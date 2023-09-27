# Narzędzie do Wykrywania Oszustw i Analizy Tekstów (CDCC 2.0)

CDCC 2.0 to zaawansowany skrypt napisany w języku Python, który służy jako wszechstronne narzędzie do wykrywania oszustw i analizy tekstów w różnych kontekstach. Oferuje ulepszoną funkcjonalność i nowe możliwości w zakresie wykrywania akademickiego plagiatu, oszustw na testach online oraz oceny autentyczności treści online.

## Wymagania

Aby uruchomić to narzędzie, będziesz potrzebować:

- Python 3.x
- Biblioteki: requests, BeautifulSoup4, scikit-learn (możesz je zainstalować za pomocą `pip install requests beautifulsoup4 scikit-learn`)

## Rozpoczęcie Pracy

Aby rozpocząć korzystanie z CDCC 2.0, postępuj zgodnie z poniższymi krokami:

1. Przejdź do katalogu, w którym znajduje się plik `main_app.py`.
2. Uruchom aplikację, wykonując polecenie `python main_app.py`.

Następnie będziesz mógł wybrać jeden z trybów i postępować zgodnie z instrukcjami wyświetlanymi na ekranie.

## Przegląd Trybów

### 1. Wykrywanie Akademickiego Plagiatu

Ten tryb umożliwia wykrywanie akademickiego plagiatu poprzez porównywanie dwóch tekstów i określanie ich podobieństwa.

### 2. Wykrywanie Oszustw na Testach Online

Użyj tego trybu do wykrywania oszustw na testach online poprzez analizę podobieństwa między dwiema udzielonymi odpowiedziami.

### 3. Sprawdzanie Autentyczności Treści Online

Ten tryb pozwala sprawdzać autentyczność treści online poprzez analizę zawartości pod kątem podejrzeń o dezinformację.

### 4. Zaawansowane Operacje Przetwarzania Tekstów

Eksploruj dodatkowe operacje przetwarzania tekstu, takie jak analiza unikalnych słów w dwóch tekstach oraz analiza częstości słów kluczowych.

## Co Nowego w CDCC 2.0

Oto kluczowe ulepszenia i nowe funkcje wprowadzone w wersji CDCC 2.0:

- **Autoryzacja**: CDCC 2.0 teraz zawiera prosty mechanizm kontroli dostępu. Użytkownicy muszą wprowadzić kod dostępu, aby korzystać z aplikacji, co zwiększa bezpieczeństwo.

- **Interfejs Graficzny (GUI)**: Aplikacja teraz posiada prosty interfejs graficzny do wprowadzania kodu dostępu, co sprawia, że jest bardziej przyjazna dla użytkownika.

- **Logowanie Wyników**: Wyniki operacji są teraz zapisywane w osobnych plikach w folderze "resources", co umożliwia użytkownikom śledzenie wyników analizy.

- **Dodatkowe Operacje Przetwarzania Tekstu**: Użytkownicy mogą teraz wykonywać zaawansowane operacje przetwarzania tekstu, takie jak analiza unikalnych słów w dwóch tekstach oraz analiza częstości słów kluczowych.

- **Udoskonalone Obsługiwanie Błędów**: Zwiększona obsługa błędów zapewnia lepszą informację zwrotną w przypadku problemów.

- **Refaktoryzacja Kodu**: Kod został zrefaktoryzowany w celu poprawy czytelności i łatwości utrzymania.

## Autorzy

CDCC 2.0 zostało opracowane przez Arkadiusza Adamowskiego [AK4CZ](https://github.com/MCakacz).

## Licencja

Ten projekt jest dostępny na licencji [MIT](https://opensource.org/licenses/MIT). Szczegóły znajdują się w pliku [LICENSE](https://github.com/MCakacz/CDCC-2.0/blob/main/LICENSE).
