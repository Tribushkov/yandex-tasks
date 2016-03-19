# tests.py
import unittest
from validate import validate_email


class ValidateTest(unittest.TestCase):

    # e-mail состоит из имени и доменной части, эти части разделяются символом "@"
    def test_email_at(self):
        self.assertTrue(validate_email('test@yandex.ru'))
        self.assertTrue(validate_email('denis@domain.com.ru'))
        self.assertFalse(validate_email('@emptyname.com'))
        self.assertFalse(validate_email('bare.string'))
        self.assertFalse(validate_email('emptydomain@'))
        self.assertFalse(validate_email('double@at@mail.com'))
        self.assertFalse(validate_email('@'))
        self.assertFalse(validate_email(''))

    # доменная часть - набор непустых строк, состоящих из символов a-z 0-9_- и разделенных точкой
    def test_domain_letters(self):
        self.assertTrue(validate_email('test@mail-test.com.ru'))
        self.assertTrue(validate_email('test@super_mail.com'))
        self.assertTrue(validate_email('test@yan-dex_99.com'))
        self.assertTrue(validate_email('test@yeah-_-wierd.com'))
        self.assertFalse(validate_email('test@a..ua'))
        self.assertFalse(validate_email('test@Yandex.com'))
        self.assertFalse(validate_email('test@test.*'))
        self.assertFalse(validate_email('test@t$#%^&()st.*'))

    # доменная часть не короче 3 символов и не длиннее 256
    def test_domain_length(self):
        self.assertFalse(validate_email('wat@.not_in_task'))
        self.assertFalse(validate_email('test@.c'))
        self.assertTrue(validate_email('test@' + 's'*253 + '.ru'))
        self.assertFalse(validate_email('test@' + 's'*254 + '.ru'))

    # каждый компонент доменной части не может начинаться или заканчиваться символом "-"
    def test_domain_pattern(self):
        self.assertFalse(validate_email('test@ya.-ru'))
        self.assertFalse(validate_email('test@ya.ru-'))
        self.assertFalse(validate_email('test@-ya.ru'))
        self.assertFalse(validate_email('test@ya-.ru'))
        self.assertTrue(validate_email('test@super-mail.com'))

    # имя (до @) не длиннее 128 символов
    def test_username_length(self):
        self.assertTrue(validate_email('c'*128 + '@mail.com'))
        self.assertFalse(validate_email('c'*129 + '@mail.com'))

    # имя состоит из символов a-z0-9"._-
    def test_user_chars(self):
        self.assertTrue(validate_email('"test.hello"_@mail.com'))
        self.assertTrue(validate_email('"hello"@mail.com'))
        self.assertTrue(validate_email('hello.99@mail.com'))
        self.assertTrue(validate_email('hel_lo-99@mail.com'))
        self.assertFalse(validate_email('USERname@mail.com'))
        self.assertFalse(validate_email('us#$*name@mail.com'))
        self.assertFalse(validate_email('hello)(&@mail.com'))
        self.assertFalse(validate_email('e!,:e@mail.com'))

    # в имени не допускаются две точки подряд;
    def test_user_dots(self):
        self.assertFalse(validate_email('test..test@ya.ru'))
        self.assertFalse(validate_email('te...st@ya.ru'))
        self.assertFalse(validate_email('....@ya.ru'))
        self.assertFalse(validate_email('..test@ya.ru'))
        self.assertFalse(validate_email('test..@ya.ru'))
        self.assertTrue(validate_email('test.test@ya.ru'))

    # если в имени и есть двойные кавычки ", то они должны быть парными
    def test_user_quotes(self):
        self.assertTrue(validate_email('hello"there"@email.net'))
        self.assertTrue(validate_email('"quotes"@email.net'))
        self.assertTrue(validate_email('""""@nice.user'))
        self.assertFalse(validate_email('three"quo"tes"@m.net'))

    # в имени могут встречаться символы "!,:", но только между парными двойными кавычками.
    def test_user_quoted(self):
        self.assertTrue(validate_email('user"!!!"@ya.ru'))
        self.assertTrue(validate_email('user"hi!"and"hi:"@ya.ru'))
        self.assertTrue(validate_email('user","@ya.ru'))
        self.assertFalse(validate_email('hel!,:lo"test"@ya.ru'))
        self.assertFalse(validate_email('hel!lo@ya.ru'))
        self.assertFalse(validate_email('hell,o@ya.ru'))
        self.assertFalse(validate_email('hel:lo@ya.ru'))
        self.assertFalse(validate_email('even"quotes!"yeap:@ya.ru'))
