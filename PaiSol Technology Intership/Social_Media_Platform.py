class User:
    def __init__(self, username):
        self.username = username
        self.friends = set()

    def add_friend(self, user):
        self.friends.add(user)
        user.friends.add(self)

    def remove_friend(self, user):
        self.friends.remove(user)
        user.friends.remove(self)


class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.comments = []

    def add_comment(self, commenter, comment):
        self.comments.append((commenter, comment))


class ListNode:
    def __init__(self, post):
        self.post = post
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_post(self, post):
        new_node = ListNode(post)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


class Graph:
    def __init__(self):
        self.graph = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []

    def add_friendship(self, user1, user2):
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)


class SocialMediaPlatform:
    def __init__(self):
        self.users = {}
        self.posts = LinkedList()
        self.friendships = Graph()

    def create_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
            self.friendships.add_user(username)

    def create_post(self, author, content):
        if author in self.users:
            post = Post(author, content)
            self.posts.add_post(post)
            return post
        else:
            print("User does not exist.")

    def add_comment_to_post(self, post, commenter, comment):
        current = self.posts.head
        while current:
            if current.post == post:
                current.post.add_comment(commenter, comment)
                break
            current = current.next
        else:
            print("Invalid post.")

    def add_friendship(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            self.friendships.add_friendship(user1, user2)
        else:
            print("One or more users do not exist.")

    def display_menu(self):
        print("\nMenu:")
        print("1. Create User")
        print("2. Create Post")
        print("3. Add Comment to Post")
        print("4. Add Friendship")
        print("5. User Details")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Enter username: ")
                self.create_user(username)
            elif choice == "2":
                author = input("Enter author's username: ")
                content = input("Enter post content: ")
                self.create_post(author, content)
            elif choice == "3":
                post_index = int(input("Enter the index of the post: "))
                commenter = input("Enter commenter's username: ")
                comment = input("Enter comment: ")
                post_node = self.posts.head
                for _ in range(post_index):
                    if post_node:
                        post_node = post_node.next
                if post_node:
                    post = post_node.post
                    self.add_comment_to_post(post, commenter, comment)
                else:
                    print("Invalid post index.")
            elif choice == "4":
                user1 = input("Enter first user's username: ")
                user2 = input("Enter second user's username: ")
                self.add_friendship(user1, user2)
            elif choice == "5":
                username = input("Enter username: ")
                self.display_user_details(username)
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_user_details(self, username):
        if username in self.users:
            user = self.users[username]
            print(f"\nUser: {username}")
            print(f"Number of posts: {self.count_user_posts(username)}")
            print(f"Number of comments: {self.count_user_comments(username)}")
            print("Posts:")
            self.display_user_posts(username)
            print(f"\nNumber of friends: {len(user.friends)}")
            print("Friends:")
            for friend in user.friends:
                print(friend.username)
        else:
            print("User does not exist.")

    def count_user_posts(self, username):
        count = 0
        current = self.posts.head
        while current:
            if current.post.author == username:
                count += 1
            current = current.next
        return count

    def count_user_comments(self, username):
        count = 0
        current = self.posts.head
        while current:
            for commenter, _ in current.post.comments:
                if commenter == username:
                    count += 1
            current = current.next
        return count

    def display_user_posts(self, username):
        current = self.posts.head
        while current:
            if current.post.author == username:
                print(f"- {current.post.content}")
                print("  Comments:")
                for commenter, comment in current.post.comments:
                    print(f"    - {commenter}: {comment}")  # Modified to include comments
            current = current.next


if __name__ == "__main__":
    social_media = SocialMediaPlatform()
    social_media.run()
