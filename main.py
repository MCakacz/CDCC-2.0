import sys
import os
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk

# Funkcja do tworzenia folderu "resources" jeśli nie istnieje
def create_resources_folder():
    folder_name = "resources"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Prosta forma zabezpieczenia - kod dostępu
def get_access_code():
    return "moj_kod_dostepu"  # Zdefiniuj swój własny kod dostępu tutaj

def authenticate_user():
    access_code = get_access_code()
    
    root = tk.Tk()
    root.title("Wprowadź kod dostępu")
    
    # Centrowanie okna na ekranie
    window_width = 300
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    
    label = tk.Label(root, text="Wprowadź kod dostępu:")
    label.pack(pady=10)
    
    entry = tk.Entry(root, show="*")  # Wprowadzone znaki będą wyświetlane jako "*"
    entry.pack(pady=5)
    
    def check_access_code():
        user_input = entry.get()
        if user_input == access_code:
            root.destroy()  # Zamknij okno po wprowadzeniu poprawnego kodu
        else:
            label.config(text="Nieprawidłowy kod dostępu. Spróbuj ponownie.")
    
    button = tk.Button(root, text="OK", command=check_access_code)
    button.pack(pady=5)
    
    root.mainloop()
    
    return True  # Założenie: użytkownik jest uwierzytelniony po poprawnym wprowadzeniu kodu

def detect_academic_cheating(text1, text2):
    # Inicjalizacja TF-IDF Vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    
    # Obliczenie TF-IDF dla tekstów
    tfidf_matrix = tfidf_vectorizer.fit_transform([text1, text2])
    
    # Obliczenie podobieństwa kosinusowego
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    
    threshold = 0.7
    
    if similarity_score >= threshold:
        result = "Teksty są podobne (podobieństwo: {:.2f})".format(similarity_score)
    else:
        result = "Teksty nie są podobne (podobieństwo: {:.2f})".format(similarity_score)
    
    # Zapisz wynik do pliku
    save_result_to_file("academic_cheating_result.txt", result)
    
    return result

def detect_online_test_cheating(answer1, answer2):
    common_keywords = set(answer1.lower().split()) & set(answer2.lower().split())
    
    cheating_threshold = 3
    
    if len(common_keywords) >= cheating_threshold:
        result = "Podejrzenie oszustwa na teście online!"
    else:
        result = "Brak podejrzenia oszustwa na teście online."
    
    # Zapisz wynik do pliku
    save_result_to_file("online_test_cheating_result.txt", result)
    
    return result

def check_online_content_authenticity(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Podniesienie wyjątku w przypadku błędu HTTP
        
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text()
        
        suspicious_keywords = ["fake news", "fałszywa informacja", "oszustwo"]
        
        for keyword in suspicious_keywords:
            if keyword in content.lower():
                result = "Podejrzenie o fałszowanie informacji na stronie {}".format(url)
                break
        else:
            result = "Treść online jest autentyczna i nie zawiera podejrzeń o fałszowanie informacji."
        
        # Zapisz wynik do pliku
        save_result_to_file("online_content_authenticity_result.txt", result)
        
        return result
    except requests.exceptions.RequestException as req_err:
        result = "Błąd podczas żądania HTTP: {}".format(req_err)
    except Exception as e:
        result = "Błąd podczas analizy treści: {}".format(str(e))
    
    # Zapisz wynik błędu do pliku
    save_result_to_file("online_content_authenticity_result.txt", result)
    
    return result


def unique_words_in_texts(text1, text2):
    words_text1 = set(text1.split())
    words_text2 = set(text2.split())
    
    unique_words = words_text1.union(words_text2)
    
    result = "Unikalne słowa w tekstach: {}".format(", ".join(unique_words))
    
    # Zapisz wynik do pliku
    save_result_to_file("unique_words_result.txt", result)
    
    return result

def keyword_frequency_analysis(text, keywords):
    keyword_count = {keyword: text.lower().count(keyword) for keyword in keywords}
    
    result = "Częstość występowania słów kluczowych:\n"
    for keyword, count in keyword_count.items():
        result += "{}: {}\n".format(keyword, count)
    
    # Zapisz wynik do pliku
    save_result_to_file("keyword_frequency_result.txt", result)
    
    return result

def save_result_to_file(filename, result):
    create_resources_folder()
    
    with open(os.path.join("resources", filename), "w", encoding="utf-8") as file:
        file.write(result)

def other_text_processing_operations():
    print("\nWybierz inną operację przetwarzania tekstu:")
    print("1. Analiza unikalnych słów w dwóch tekstach")
    print("2. Analiza częstości słów kluczowych w tekście")
    print("3. Powrót do menu głównego")
    
    choice = input("Wybierz opcję (1/2/3): ")
    
    if choice == "1":
        text1 = input("Wprowadź pierwszy tekst: ")
        text2 = input("Wprowadź drugi tekst: ")
        result = unique_words_in_texts(text1, text2)
        print(result)
    elif choice == "2":
        text = input("Wprowadź tekst: ")
        keywords = input("Podaj słowa kluczowe oddzielone spacją: ").split()
        result = keyword_frequency_analysis(text, keywords)
        print(result)
    elif choice == "3":
        return
    else:
        print("Niepoprawny wybór. Wybierz opcję 1, 2 lub 3.")

def main_menu():
    authenticated = False  # Użytkownik nie jest uwierzytelniony na początku
    while not authenticated:
        authenticated = authenticate_user()
    
    while True:
        print("\nWybierz tryb:")
        print("1. Akademicki Plagiat")
        print("2. Oszustwa na Testach Online")
        print("3. Podejrzenia o Fałszowanie Informacji w Treściach Online")
        print("4. Inne operacje związane z przetwarzaniem tekstu")
        print("5. Wyjście z aplikacji")
        
        wybor = input("Wybierz opcję (1/2/3/4/5): ")
        
        if wybor == "1":
            text1 = input("Wprowadź pierwszy tekst: ")
            text2 = input("Wprowadź drugi tekst: ")
            result = detect_academic_cheating(text1, text2)
            print(result)
        elif wybor == "2":
            answer1 = input("Wprowadź pierwszą odpowiedź: ")
            answer2 = input("Wprowadź drugą odpowiedź: ")
            result = detect_online_test_cheating(answer1, answer2)
            print(result)
        elif wybor == "3":
            url = input("Wprowadź URL treści online do analizy: ")
            result = check_online_content_authenticity(url)
            print(result)
        elif wybor == "4":
            other_text_processing_operations()
        elif wybor == "5":
            print("Wyjście z aplikacji.")
            break
        else:
            print("Niepoprawny wybór. Wybierz opcję 1, 2, 3, 4 lub 5.")

if __name__ == "__main__":
    main_menu()
