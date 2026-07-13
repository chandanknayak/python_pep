class Node:
    def __init__(self, card=None):
        self.card = card
        self.prev = None
        self.next = None


class CardHand:
    def __init__(self):
        # Doubly Linked List
        self.head = None
        self.tail = None

        # Four fingers (last node of each suit)
        self.fingers = {
            "hearts": None,
            "clubs": None,
            "spades": None,
            "diamonds": None
        }

        self.order = ["hearts", "clubs", "spades", "diamonds"]

    # -----------------------------
    # Insert node after given node
    # -----------------------------
    def insert_after(self, node, new_node):
        if node is None:
            # Insert at beginning
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            new_node.next = node.next
            new_node.prev = node

            if node.next:
                node.next.prev = new_node
            else:
                self.tail = new_node

            node.next = new_node

    # -----------------------------
    # Add Card
    # -----------------------------
    def add_card(self, rank, suit):
        card = (rank, suit)
        new_node = Node(card)

        # If suit already exists
        if self.fingers[suit]:
            self.insert_after(self.fingers[suit], new_node)
            self.fingers[suit] = new_node
            return

        # Find previous suit having cards
        previous = None
        idx = self.order.index(suit)

        for i in range(idx - 1, -1, -1):
            prev_suit = self.order[i]
            if self.fingers[prev_suit]:
                previous = self.fingers[prev_suit]
                break

        self.insert_after(previous, new_node)
        self.fingers[suit] = new_node

    # -----------------------------
    # Remove node
    # -----------------------------
    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    # -----------------------------
    # Play Card
    # -----------------------------
    def play(self, suit):
        current = self.head

        while current:
            if current.card[1] == suit:
                self.remove_node(current)

                if self.fingers[suit] == current:
                    temp = current.prev
                    if temp and temp.card[1] == suit:
                        self.fingers[suit] = temp
                    else:
                        self.fingers[suit] = None

                return current.card

            current = current.next

        # If suit not found, remove first card
        if self.head:
            card = self.head.card
            self.remove_node(self.head)
            return card

        return None

    # -----------------------------
    # Iterate all cards
    # -----------------------------
    def __iter__(self):
        current = self.head
        while current:
            yield current.card
            current = current.next

    # -----------------------------
    # Iterate all cards of one suit
    # -----------------------------
    def all_of_suit(self, suit):
        current = self.head
        while current:
            if current.card[1] == suit:
                yield current.card
            current = current.next


# -----------------------------
# Driver Program
# -----------------------------

hand = CardHand()

hand.add_card("A", "hearts")
hand.add_card("10", "spades")
hand.add_card("K", "hearts")
hand.add_card("7", "clubs")
hand.add_card("5", "diamonds")
hand.add_card("Q", "spades")

print("All Cards:")
for card in hand:
    print(card)

print("\nHearts:")
for card in hand.all_of_suit("hearts"):
    print(card)

print("\nPlayed:", hand.play("spades"))

print("\nAfter Playing:")
for card in hand:
    print(card)
