import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        collector = BooksCollector()
        return collector

    books_genre_list = [
            ['Тайна третьей планеты', 'Фантастика'],
            ['Дракула', 'Ужасы'],
            ['Печальный кипарис', 'Детективы'],
            ['Зверский детектив', 'Мультфильмы'],
            ['Полный порядок, Дживс!', 'Комедии']
        ]

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name, genre', books_genre_list)
    def test_set_book_genre_set_genre_from_list(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    def test_get_book_genre_get_book_genre_for_book_without_genre(self, collector):
        collector.add_new_book('Дракула')
        assert collector.get_book_genre('Дракула') == ''

    @pytest.mark.parametrize('name, genre', books_genre_list)
    def test_get_books_with_specific_genre_get_books_with_genre_from_list(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_genre_get_dict_with_one_book(self, collector):
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.books_genre == {'Дракула': 'Ужасы'}

    def test_get_books_for_children_get_books_without_genre_age_rating(self, collector):
        collector.add_new_book('Тайна третьей планеты')
        collector.set_book_genre('Тайна третьей планеты', 'Фантастика')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.get_books_for_children() == ['Тайна третьей планеты']

    def test_add_book_in_favorites_add_book_from_dict(self, collector):
        collector.add_new_book('Тайна третьей планеты')
        collector.add_book_in_favorites('Тайна третьей планеты')
        assert collector.favorites == ['Тайна третьей планеты']

    def test_delete_book_from_favorites_delete_only_book_from_favorites(self, collector):
        collector.add_new_book('Тайна третьей планеты')
        collector.add_book_in_favorites('Тайна третьей планеты')
        collector.delete_book_from_favorites('Тайна третьей планеты')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_get_list_of_added_favorite_books(self, collector):
        collector.add_new_book('Тайна третьей планеты')
        collector.add_new_book('Дракула')
        collector.add_book_in_favorites('Тайна третьей планеты')
        collector.add_book_in_favorites('Дракула')
        assert collector.get_list_of_favorites_books() == ['Тайна третьей планеты', 'Дракула']
