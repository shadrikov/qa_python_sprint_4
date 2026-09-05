import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # следующая строка закомментирована, т.к. в классе BooksCollector не существует метода get_books_rating 
        # assert len(collector.get_books_rating()) == 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тестирование метода add_new_book: книги с невалидной длиной наименования не добавляются словарь
    @pytest.mark.parametrize('invalid_name_length', ['', 'Тестовое наименование, в котором больше 41 символа'])

    def test_add_new_book_invalid_name_length_not_in_books_genre(self, invalid_name_length):
        collector = BooksCollector()
        collector.add_new_book(invalid_name_length)
        assert invalid_name_length not in collector.books_genre

    # тестирование метода set_book_genre: жанр не из списка genre не устанавливается для книг
    def test_set_book_genre_invalid_genre_hasnt_set(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', 'Драма')
        assert collector.books_genre['Война и мир'] == ''

    # тестирование метода get_book_genre: возвращается жанр существующей книги
    def test_get_book_genre_return_genre_of_the_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Убежище')
        collector.set_book_genre('Убежище', 'Фантастика')
        assert collector.get_book_genre('Убежище') == 'Фантастика'

    # тестирование метода get_books_with_specific_genre: возвращаются все книги указанного жанра
    def test_get_books_with_specific_genre_return_books_of_the_specified_genre(self):
        collector = BooksCollector()
        books = {
            'Метро 2033': 'Фантастика',
            'Пост': 'Фантастика',
            '12 стульев': 'Комедии'
            }
        for key, value in books.items():
            collector.add_new_book(key)
            collector.set_book_genre(key, value)
        books_with_specific_genre = collector.get_books_with_specific_genre('Фантастика')
        assert 'Метро 2033' in books_with_specific_genre and 'Пост' in books_with_specific_genre and '12 стульев' not in books_with_specific_genre

    # тестирование метода get_books_genre: для нового объекта класса возвращается пустой словарь
    def test_get_books_genre_return_empty_dictionary_when_no_books(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {}

    # тестирование метода get_books_for_children: книги с возрастным рейтингом не возвращаются
    def test_get_books_for_children_do_not_return_books_with_age_rating(self):
        collector = BooksCollector()
        books = {
            'Метро 2033': 'Фантастика',
            'Оно': 'Ужасы',
            'Остров проклятых': 'Детективы'
            }
        for key, value in books.items():
            collector.add_new_book(key)
            collector.set_book_genre(key, value)
        assert collector.get_books_for_children() == ['Метро 2033']

    # тестирование метода add_book_in_favorites: существующая книга добавляется в избранное
    def test_add_book_in_favorites_add_existing_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_book_in_favorites('Преступление и наказание')
        assert 'Преступление и наказание' in collector.favorites

    # тестирование метода delete_book_from_favorites: существующая книга удаляется из избранного
    def test_delete_book_from_favorites_remove_existing_book_from_favorites(self):
        collector = BooksCollector()
        books = ['Маленький принц', 'Капитанская дочка']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites('Маленький принц')
        assert 'Маленький принц' not in collector.favorites

    # тестирование метода get_list_of_favorites_books: возвращается список избранных книг
    def test_get_list_of_favorites_books_return_favorites_books(self):
        collector = BooksCollector()
        books = ['Отцы и дети', 'Горе от ума', 'Мёртвые души']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        assert 'Отцы и дети' in collector.get_list_of_favorites_books() and 'Горе от ума' in collector.get_list_of_favorites_books() and 'Мёртвые души' in collector.get_list_of_favorites_books()

