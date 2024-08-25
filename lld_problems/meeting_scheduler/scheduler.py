from dataclasses import dataclass, field
from typing import List, Optional
from collections import defaultdict, OrderedDict
import uuid
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class User:
    name: str
    email: str


@dataclass
class Interval:
    start_time: int
    end_time: int


@dataclass
class Meetings:
    id: str
    start_time: int
    end_time: int
    invitees: List[User]


@dataclass
class MailClient:
    def send_mail(self, email: str):
        logger.info(f"Sending mail to this id {email}")


@dataclass
class Calendar:
    meetings_list: List[Meetings] = field(default_factory=list)
    calendar: OrderedDict = field(default_factory=OrderedDict)

    def check_availability(self, interval: Interval) -> bool:
        for meeting in self.meetings_list:
            start_time = meeting.start_time
            end_time = meeting.end_time
            self.calendar[start_time] = end_time

        prev = max((k for k in self.calendar.keys() if k <= interval.start_time), default=None)
        next = min((k for k in self.calendar.keys() if k > interval.start_time), default=None)

        if (prev is None or self.calendar[prev] <= interval.start_time) and \
                (next is None or interval.end_time <= next):
            return True
        return False

    def add_meeting(self, meeting: Meetings):
        self.calendar[meeting.start_time] = meeting.end_time
        self.meetings_list.append(meeting)


@dataclass
class MeetingRoom:
    id: int
    capacity: int
    calendar: Calendar
    mail_client: MailClient

    def check_availability(self, interval: Interval) -> bool:
        return self.calendar.check_availability(interval)

    def book_meeting_room(self, interval: Interval, users: List[User]) -> Meetings:
        meeting = Meetings(
            id=str(uuid.uuid4()),
            start_time=interval.start_time,
            end_time=interval.end_time,
            invitees=users
        )
        self.calendar.add_meeting(meeting)
        for user in users:
            self.mail_client.send_mail(user.email)
        return meeting


@dataclass
class MeetingRoomScheduler:
    meeting_room_list: List[MeetingRoom]

    def book_meeting_room(self, interval: Interval, users: List[User]) -> Optional[Meetings]:
        for meeting_room in self.meeting_room_list:
            if len(users) <= meeting_room.capacity:
                if meeting_room.check_availability(interval):
                    meeting_details = meeting_room.book_meeting_room(interval, users)
                    logger.info(f"Booked meeting in room {meeting_room.id} with details {meeting_details}")
                    return meeting_details
        logger.info("No meeting room found as of now for your time")
        return None


if __name__ == "__main__":
    user1 = User(name="Alice", email="alice@example.com")
    user2 = User(name="Bob", email="bob@example.com")
    user3 = User(name="Charlie", email="charlie@example.com")

    # Create a mail client
    mail_client = MailClient()

    # Create calendars for meeting rooms
    calendar1 = Calendar()
    calendar2 = Calendar()

    # Create meeting rooms
    meeting_room1 = MeetingRoom(id=1, capacity=2, calendar=calendar1, mail_client=mail_client)
    meeting_room2 = MeetingRoom(id=2, capacity=3, calendar=calendar2, mail_client=mail_client)

    # Create a meeting room scheduler
    scheduler = MeetingRoomScheduler(meeting_room_list=[meeting_room1, meeting_room2])

    # Define a time interval for the meeting
    interval = Interval(start_time=10, end_time=12)

    # Try to book a meeting room for Alice and Bob
    meeting1 = scheduler.book_meeting_room(interval, users=[user1, user2])
    if meeting1:
        print(f"Meeting booked: {meeting1}")
    else:
        print("No meeting room available for Alice and Bob at this time.")

    # Define another time interval that overlaps with the first
    overlapping_interval = Interval(start_time=11, end_time=13)

    # Try to book a meeting room for Charlie
    meeting2 = scheduler.book_meeting_room(overlapping_interval, users=[user3])
    if meeting2:
        print(f"Meeting booked: {meeting2}")
    else:
        print("No meeting room available for Charlie at this time.")

