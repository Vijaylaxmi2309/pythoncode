##python 1. Answer
def count_word_frequency(input_string):
    word_frequency = {}
    
    # Split the string into words
    words = input_string.split()
    
    # Count the frequency of each word
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    
    # Find the highest frequency
    max_frequency = max(word_frequency.values())
    
    # Find the length of the highest-frequency word
    max_frequency_word_length = max(len(word) for word, frequency in word_frequency.items() if frequency == max_frequency)
    
    return max_frequency_word_length


# Example usage
input_string = "write write write all the number from from from 1 to 1000"
result = count_word_frequency(input_string)
print(result)


##python 2. Answer
from collections import Counter
def is_valid_string(s):
    # Count the frequency of each character
    char_counts = Counter(s)

    # Get the frequencies of the characters
    frequencies = list(char_counts.values())

    # If all frequencies are the same, the string is valid
    if len(set(frequencies)) == 1:
        return "YES"

    # If there are more than two unique frequencies, it's not valid
    if len(set(frequencies)) > 2:
        return "NO"

    # If there are exactly two unique frequencies, check if we can remove a character
    # to make the remaining characters have the same frequency
    frequency_count = list(char_counts.items())
    char1, freq1 = frequency_count[0]
    char2, freq2 = frequency_count[1]

    # Check if removing one character makes the remaining characters have the same frequency
    if (freq1 == 1 and freq2 == len(s) - 1) or (freq2 == 1 and freq1 == len(s) - 1):
        return "YES"

    return "NO"

# Example usage
input_string = "aabbc"
result = is_valid_string(input_string)
print(result)

input_string = "abcabc"
result = is_valid_string(input_string)
print(result)


##python 3.Answer
import pandas as pd
import requests

# Download the JSON data
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

# Extract relevant data attributes
pokemon_list = data["pokemon"]
rows = []
for pokemon in pokemon_list:
    row = {
        "id": pokemon.get("id"),
        "num": pokemon.get("num"),
        "name": pokemon.get("name"),
        "img": pokemon.get("img"),
        "type": ", ".join(pokemon.get("type", [])),
        "height": pokemon.get("height"),
        "weight": pokemon.get("weight"),
        "candy": pokemon.get("candy"),
        "candy_count": pokemon.get("candy_count"),
        "egg": pokemon.get("egg"),
        "spawn_chance": pokemon.get("spawn_chance"),
        "avg_spawns": pokemon.get("avg_spawns"),
        "spawn_time": pokemon.get("spawn_time"),
        "weakness": ", ".join(pokemon.get("weaknesses", []))
    }
    rows.append(row)

# Create a DataFrame from the extracted data
df = pd.DataFrame(rows)

# Convert DataFrame to Excel format
excel_file = "pokemon_data.xlsx"
df.to_excel(excel_file, index=False)

print("Data has been converted and saved to", excel_file)


##python 5.Answer
import requests
import json
from bs4 import BeautifulSoup

# Download the data from the provided API link
url = 'http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes'
response = requests.get(url)
data = response.json()

# Extract relevant data attributes and create a dictionary
episode = data['_embedded']['episodes'][0]  # Assuming we only need the first episode
formatted_data = {
    'id': episode['id'],
    'url': episode['url'],
    'name': episode['name'],
    'season': episode['season'],
    'number': episode['number'],
    'type': episode['type'],
    'airdate': episode['airdate'],
    'airtime': episode['airtime'],
    'airstamp': episode['airstamp'],
    'runtime': episode['runtime'],
    'rating': {
        'average': episode['rating']['average']
    },
    'image': {
        'medium': episode['image']['medium'],
        'original': episode['image']['original']
    },
    'summary': BeautifulSoup(episode['summary'], 'html.parser').get_text(),
    '_links': {
        'self': {
            'href': episode['_links']['self']['href']
        },
        'show': {
            'href': episode['_links']['show']['href']
        }
    }
}

# Convert the formatted data to JSON
output_data = json.dumps(formatted_data, indent=4)

# Print the output JSON data
print(output_data)


##python 6.Answer
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Download the JSON data from the provided link
url = 'https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json'
response = requests.get(url)
data = response.json()

# Create a DataFrame from the JSON data
df = pd.DataFrame(data['pokemon'])

# Convert spawn_chance column to numeric
df['spawn_chance'] = pd.to_numeric(df['spawn_chance'], errors='coerce')

# Question 1: Get all Pokemons whose spawn rate is less than 5%
spawn_rate_threshold = 5
spawn_rate_lt_5 = df[df['spawn_chance'] < spawn_rate_threshold]
print("Pokemons with spawn rate less than 5%:")
print(spawn_rate_lt_5[['name', 'spawn_chance']])
print()

# Question 2: Get all Pokemons that have less than 4 weaknesses
max_weaknesses = 4
weaknesses_lt_4 = df[df['weaknesses'].str.len() < max_weaknesses]
print("Pokemons with less than 4 weaknesses:")
print(weaknesses_lt_4[['name', 'weaknesses']])
print()


# Plots for better visualizations

# Bar plot: Spawn rate distribution
plt.figure(figsize=(10, 6))
plt.hist(df['spawn_chance'].dropna(), bins=20, color='steelblue')
plt.xlabel('Spawn Rate')
plt.ylabel('Count')
plt.title('Spawn Rate Distribution')
plt.grid(True)
plt.show()

# Bar plot: Number of weaknesses distribution
plt.figure(figsize=(10, 6))
plt.hist(df['weaknesses'].str.len(), bins=range(1, 13), color='steelblue')
plt.xlabel('Number of Weaknesses')
plt.ylabel('Count')
plt.title('Number of Weaknesses Distribution')
plt.grid(True)
plt.show()

# Pie chart: Types of capabilities distribution
type_counts = df['type'].str.len().value_counts()
labels = type_counts.index.astype(str)
sizes = type_counts.values
explode = [0.1 if l == '1' else 0 for l in labels]
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90)
plt.title('Types of Capabilities Distribution')
plt.axis('equal')
plt.show()

##python 8.Answer
import requests
import matplotlib.pyplot as plt

# Download the JSON data
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = response.json()

# Extract relevant data attributes
seasons = data["_embedded"]["episodes"]

# Question 1: Get all the overall ratings for each season and compare them using plots
season_ratings = []
season_numbers = []
for season in seasons:
    season_number = season["season"]
    episode_rating = season["rating"]["average"]
    season_ratings.append(float(episode_rating))
    season_numbers.append(int(season_number))

# Plotting the ratings for each season
plt.figure(figsize=(8, 6))
plt.plot(season_numbers, season_ratings, marker='o', linestyle='-', color='blue')
plt.title("Westworld Season Ratings")
plt.xlabel("Season Number")
plt.ylabel("Average Rating")
plt.grid(True)
plt.show()

# Question 2: Get all the episode names with an average rating above 8 for every season
highly_rated_episodes = []
for season in seasons:
    season_number = season["season"]
    episode_name = season["name"]
    episode_rating = float(season["rating"]["average"])
    if episode_rating > 8:
        highly_rated_episodes.append((season_number, episode_name))

# Question 3: Get all the episode names that aired before May 2019
episodes_before_may_2019 = []
for season in seasons:
    episode_name = season["name"]
    episode_airdate = season["airdate"]
    if episode_airdate < "2019-05-01":
        episodes_before_may_2019.append(episode_name)

# Question 4: Get the episode name with the highest and lowest rating from each season
highest_rated_episodes = {}
lowest_rated_episodes = {}
for season in seasons:
    season_number = season["season"]
    episode_name = season["name"]
    episode_rating = float(season["rating"]["average"])
    if season_number not in highest_rated_episodes:
        highest_rated_episodes[season_number] = (episode_name, episode_rating)
        lowest_rated_episodes[season_number] = (episode_name, episode_rating)
    else:
        if episode_rating > highest_rated_episodes[season_number][1]:
            highest_rated_episodes[season_number] = (episode_name, episode_rating)
        if episode_rating < lowest_rated_episodes[season_number][1]:
            lowest_rated_episodes[season_number] = (episode_name, episode_rating)

# Question 5: Get the summary for the most popular (highest rated) episode in every season
most_popular_episodes = {}
for season in seasons:
    season_number = season["season"]
    episode_name = season["name"]
    episode_rating = float(season["rating"]["average"])
    episode_summary = season["summary"]
    if season_number not in most_popular_episodes:
        most_popular_episodes[season_number] = (episode_name, episode_rating, episode_summary)
    else:
        if episode_rating > most_popular_episodes[season_number][1]:
            most_popular_episodes[season_number] = (episode_name, episode_rating, episode_summary)

# Print the results
print("Overall Ratings for Each Season:", season_ratings)
print("Highly Rated Episodes (> 8):", highly_rated_episodes)
print("Episodes Aired Before May 2019:", episodes_before_may_2019)
print("Highest Rated Episode from Each Season:", highest_rated_episodes)
print("Lowest Rated Episode from Each Season:", lowest_rated_episodes)
print("Most Popular Episode from Each Season:")
for season, episode_info in most_popular_episodes.items():
    print("Season", season, ":", episode_info[0])
    print("Summary:", episode_info[2])
    print("---------------------------------------------")


##python 9.Answer
import requests
import matplotlib.pyplot as plt

# Download the JSON data
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = response.json()

# Extract relevant data attributes
seasons = data["_embedded"]["episodes"]

# Question 1: Get all the overall ratings for each season and compare them using plots
season_ratings = []
season_numbers = []
for season in seasons:
    season_number = season["season"]
    episode_rating = season["rating"]["average"]
    season_ratings.append(float(episode_rating))
    season_numbers.append(int(season_number))

# Plotting the ratings for each season
plt.figure(figsize=(8, 6))
plt.plot(season_numbers, season_ratings, marker='o', linestyle='-', color='blue')
plt.title("Westworld Season Ratings")
plt.xlabel("Season Number")
plt.ylabel("Average Rating")
plt.grid(True)
plt.show()

# Question 2: Get all the episode names with an average rating above 8 for every season
highly_rated_episodes = []
for season in seasons:
    season_number = season["season"]
    episode_name = season["name"]
    episode_rating = float(season["rating"]["average"])
    if episode_rating > 8:
        highly_rated_episodes.append((season_number, episode_name))

# Question 3: Get all the episode names that aired before May 2019
episodes_before_may_2019 = []
for season in seasons:
    episode_name = season["name"]
    episode_airdate = season["airdate"]
    if episode_airdate < "2019-05-01":
        episodes_before_may_2019.append(episode_name)

# Question 4: Get the episode name with the highest and lowest rating from each season
highest_rated_episodes = {}
lowest_rated_episodes = {}
for season in seasons:
    season_number = season["season"]
    episode_name = season["name"]
    episode_rating = float(season["rating"]["average"])
    if season_number not in highest_rated_episodes:
        highest_rated_episodes[season_number] = (episode_name, episode_rating)
        lowest_rated_episodes[season_number] = (episode_name, episode_rating)
    else:
        if episode_rating > highest_rated_episodes[season_number][1]:
            highest_rated_episodes[season_number] = (episode_name, episode_rating)
        if episode_rating < lowest_rated_episodes[season_number][1]:
            lowest_rated_episodes[season_number] = (episode_name, episode_rating)

# Question 5: Get the summary for the most popular (highest rated) episode in every season
most_popular_episodes = {}
for season in seasons:
    season_number = season["season"]
    episode_name = season["name"]
    episode_rating = float(season["rating"]["average"])
    episode_summary = season["summary"]
    if season_number not in most_popular_episodes:
        most_popular_episodes[season_number] = (episode_name, episode_rating, episode_summary)
    else:
        if episode_rating > most_popular_episodes[season_number][1]:
            most_popular_episodes[season_number] = (episode_name, episode_rating, episode_summary)

# Print the results
print("Overall Ratings for Each Season:", season_ratings)
print("Highly Rated Episodes (> 8):", highly_rated_episodes)
print("Episodes Aired Before May 2019:", episodes_before_may_2019)
print("Highest Rated Episode from Each Season:", highest_rated_episodes)
print("Lowest Rated Episode from Each Season:", lowest_rated_episodes)
print("Most Popular Episode from Each Season:")
for season, episode_info in most_popular_episodes.items():
    print("Season", season, ":", episode_info[0])
    print("Summary:", episode_info[2])
    print("---------------------------------------------")
