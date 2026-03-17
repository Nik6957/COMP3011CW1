import sqlite3

# Connect to the database
conn = sqlite3.connect('rewards.db')
cursor = conn.cursor()

# 20 Realistic UK Reward Programs
uk_rewards = [
    ('Amex Gold Preferred', 20000),
    ('Nectar Card (Sainsbury\'s)', 1250),
    ('Tesco Clubcard', 800),
    ('Boots Advantage Card', 2400),
    ('British Airways Executive Club', 15000),
    ('Virgin Atlantic Flying Club', 12000),
    ('Marriott Bonvoy', 5000),
    ('Hilton Honors', 8500),
    ('Barclays Avios Rewards', 3000),
    ('HSBC Rewards', 4200),
    ('Marks & Spencer Sparks', 150),
    ('Co-op Membership', 450),
    ('Waitrose & Partners', 100),
    ('Costa Coffee Club', 25),
    ('Starbucks Rewards', 12),
    ('Subway Rewards', 500),
    ('Waterstones Plus', 10),
    ('H&M Membership', 200),
    ('IKEA Family Points', 0),
    ('Shell Go+', 120)
]

# Insert the data
cursor.executemany('INSERT INTO rewards (name, points) VALUES (?, ?)', uk_rewards)

# Save and close
conn.commit()
conn.close()

print("Successfully seeded 20 UK reward programs into rewards.db!")