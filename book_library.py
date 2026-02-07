# Simple Book Library Management Program
# This program allows the user to manage owned books and a wishlist

# Lists to store books
your_library = []
wishlist = []

# Add books you own
book = input("Enter the name of a book you own: ")
your_library.append(book)

another_book = input("Enter another book you own (or press Enter to skip): ")
if another_book:
    your_library.append(another_book)

print(f"Your library: {your_library}")

# Add books to wishlist
wish = input("Enter the name of a book you wish to have in the future: ")
wishlist.append(wish)

another_wish = input(
    "Enter another book you wish to have in the future (or press Enter to skip): "
)
if another_wish:
    wishlist.append(another_wish)

print(f"Your wishlist: {wishlist}")

# Acquire a book from wishlist
acquired = input(
    "Enter the name of a book from your wishlist you have acquired (or press Enter to skip): "
)
if acquired in wishlist:
    wishlist.remove(acquired)
    your_library.append(acquired)

print(f"Updated library: {your_library}")
print(f"Updated wishlist: {wishlist}")

# Donate a book
donation = input(
    "Enter the name of a book you wish to donate (or press Enter to skip): "
)
if donation in your_library:
    your_library.remove(donation)

print(f"Final library: {your_library}")
