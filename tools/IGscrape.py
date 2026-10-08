import instaloader

class IGScrape:
    """
    Scrapes data from an Instagram account using instaloader.

    :param target: The username of the account to scrape.
    """
    def __init__(self, target) -> None:
        self.target = target
        self.loader = instaloader.Instaloader()

        print(f"Trying to scrape information about {target}...")

        try:
            profile = instaloader.Profile.from_username(self.loader.context, self.target)
            self.print_user_info(profile)
        except Exception as e:
            print(f"Error: {e}")
            return

    def print_user_info(self, profile) -> None:

        readable_data = {
            'Username': profile.username,
            'Full Name': profile.full_name,
            'Biography': profile.biography,
            'Website': profile.external_url if profile.external_url else 'N/A',
            'Followers': profile.followers,
            'Following': profile.followees,
            'Profile Picture URL': profile.profile_pic_url,
            'Is Private': profile.is_private,
            'Is Verified': profile.is_verified,
            'Total Posts': profile.mediacount
        }

        for key, value in readable_data.items():
            print(f"{key} : {value}")

if __name__ == "__main__":
    username = input("Enter the Instagram username: ").strip()
    IGScrape(username)
