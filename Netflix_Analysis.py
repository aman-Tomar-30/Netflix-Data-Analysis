import pandas as pd
import matplotlib.pyplot as plt
print("Imported Successfully")

# load data
data = pd.read_csv("Netflix_Dataset.csv")
print(data.head())

# Clean dataset
data = data.dropna(subset=['Director', 'Cast', 'Country', 'Release_Date', 'Rating', 'Duration', 'Type', 'Description'])
print(data)

# Movie VS Tv Shows

count_type = data["Category"].value_counts()
print(count_type)
plt.figure(figsize=(6,4))
plt.bar(count_type.index, count_type.values, color=['blue','yellow'])
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Number of Movie And Tv Shows on Netflix")
plt.tight_layout()
# plt.savefig("movie_tvShows.png", dpi=300)
plt.show()

# Rating Percentage

rating_counts = data["Rating"].value_counts()
print(rating_counts)
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Percentage of content Rating on Netflix")
# plt.savefig("content_rating.png")
plt.tight_layout()
plt.show()

# Duration Distribution of Movie

movie_data = data[data["Category"] == "Movie"].copy()
movie_data["duration_int"] = movie_data["Duration"].str.replace(" min","").astype(int)
print(movie_data.head())
plt.figure(figsize=(8,6))
plt.hist(movie_data["duration_int"], bins=30, color='grey', edgecolor='purple')
plt.xlabel("Duration (in Min)")
plt.ylabel("Number of Movies")
plt.title('Movie Distribution based on Duration')
plt.tight_layout()
# plt.savefig("Time_distribution_of_movie.png")
plt.show()

# Relationship between releasing year and no.of movies
movie_data["Release_Year"] = movie_data["Release_Date"].str[-4:].astype(int)
# print(movie_data["Release_Year"].head())

movie_count_per_year = movie_data["Release_Year"].value_counts().sort_index()
print(movie_count_per_year.head())
plt.figure(figsize=(8,6))
plt.scatter(movie_count_per_year.index, movie_count_per_year.values, color='purple')
plt.title("Release Year Vs No.of Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.show()


# Most release given by the country
country_count = data["Country"].value_counts().head(10)
# print(country_count)
plt.figure(figsize=(8,6))
plt.barh(country_count.index, country_count.values, color='teal')
plt.title("Top 10 Countries by Number of Shows")
plt.xlabel("Number of Shows")
plt.ylabel("Country")
plt.tight_layout()
plt.show()


# Subplotting
data["Release_Year"] = data["Release_Date"].str[-4:].astype(int)
content_by_year = data.groupby(["Release_Year", "Category"]).size().unstack().fillna(0)
print(content_by_year.head())
fig, ax = plt.subplots(1,2,figsize=(12,5))
# Subplot- Movie
ax[0].plot(content_by_year.index, content_by_year.Movie, color='purple')
ax[0].set_title("Movies Released Per Year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")
# Subplot - Tv Shows
ax[1].plot(content_by_year.index, content_by_year["TV Show"], color='red')
ax[1].set_title("Tv Shows Released Per Year")
ax[1].set_xlabel("Year")
ax[1].set_ylabel("Number of Tv Shows")
fig.suptitle("Comparison of Movie and Tv Shows Over Years")
plt.tight_layout()
plt.show()
