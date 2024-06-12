class Article:
    all = []  # Class attribute to store all Article instances

    def __init__(self, author, magazine, title):
        self.author = author  # Associate the article with an author
        self.magazine = magazine  # Associate the article with a magazine
        self.title = title  # Set the article title

        # Validate the title length
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title

        # Add the article to the list of all articles
        Article.all.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Validate the title is a string between 5 and 50 characters
        if isinstance(value, str) and len(value) >= 5 and len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        # Ensure the author is an instance of the Author class
        if isinstance(value, Author):
            self._author = value
        else:
            raise TypeError("Author must be an instance of the Author class")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Ensure the magazine is an instance of the Magazine class
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise TypeError("Magazine must be an instance of the Magazine class")


class Author:
    def __init__(self, name):
        # Validate the name is a non-empty string
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        # Return a list of all articles written by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Return a list of unique magazines the author has written for
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        # Create a new article associated with this author and the given magazine
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        # Return a list of unique topic areas (magazine categories) the author has written about
        magazine_categories = [magazine.category for magazine in self.magazines()]
        if not magazine_categories:
            return None
        return list(set(magazine_categories))


class Magazine:
    _magazines = []

    def __init__(self, name, category):
        # Validate the name and category
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []
        Magazine._magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        # Return a list of all articles associated with this magazine
        return self._articles

    def contributors(self):
        # Return a list of unique authors who have written articles for this magazine
        return list(set([article.author for article in self._articles]))

    def article_titles(self):
        # Return a list of titles for all articles associated with this magazine
        articles = self._articles
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        # Return a list of authors who have written more than 2 articles for this magazine
        author_count = {}
        for article in self._articles:
            author = article.author
            if author in author_count:
                author_count[author] += 1
            else:
                author_count[author] = 1

        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

    @classmethod
    def top_publisher(cls):
        # Return the magazine with the most articles
        if not cls._magazines:
            return None
        return max(cls._magazines, key=lambda magazine: len(magazine._articles))
