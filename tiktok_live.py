import io

from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@ninkogmari")
#client: TikTokLiveClient = TikTokLiveClient(unique_id="@rachelthaqueen2")
#client: TikTokLiveClient = TikTokLiveClient(unique_id="@team_hassan1")


@client.on("comment")
async def on_comment(event: CommentEvent):

    print(f"{event.user.nickname} -> {event.comment}")


    """

    Downloading an avatar to bytes is very easy.
    It uses the instance of TikTokLiveClient that the event belongs to.
    Specifically, it borrows the TikTokLiveClient's HTTP Client.

    This example downloads an image and displays it via Pillow (PIL)
    whenever a user comments on the TikTok LIVE.

    """

@client.on("gift")
async def on_gift(event: GiftEvent):
    """
    This is an example for the "gift" event to show you how to read gift data properly.

    Important Note:

    Gifts of type 1 can have streaks, so we need to check that the streak has ended
    If the gift type isn't 1, it can't repeat. Therefore, we can go straight to printing

    """

    # Streakable gift & streak is over
    if event.gift.streakable and not event.gift.streaking:
        print(f"{event.user.unique_id} sent {event.gift.count}x \"{event.gift.info.type}\" - \"{event.gift.info.name}\" ")

    # Non-streakable gift
    elif not event.gift.streakable:
        print(f"{event.user.unique_id} sent \"{event.gift.info.name}\"")


if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
