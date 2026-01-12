import json
import requests
import time
import os

# Kitoblar ro'yxatini o'qish
with open('public/books.json', 'r', encoding='utf-8') as f:
    books = json.load(f)

# Rasmlar papkasini yaratish
os.makedirs('public/books', exist_ok=True)

updated_books = []

for i, book in enumerate(books):
    print(f"[{i+1}/{len(books)}] {book['title']} qidirilmoqda...")
    
    try:
        # API dan qidirish
        search_query = book['title']
        url = f"https://api.mutolaa.com/api/v1/book/web/BookList/?offset=0&limit=5&search={search_query}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('results') and len(data['results']) > 0:
                # Eng mos kitobni topish
                found = None
                for result in data['results']:
                    if book['title'].lower() in result['title'].lower() or result['title'].lower() in book['title'].lower():
                        found = result
                        break
                
                if not found:
                    found = data['results'][0]
                
                # Ma'lumotlarni yangilash
                book['api_title'] = found.get('title', '')
                book['description'] = found.get('description', '')
                book['slug'] = found.get('slug', '')
                book['image'] = found.get('image', '')
                
                # Rasmni yuklab olish
                if found.get('image'):
                    try:
                        img_response = requests.get(found['image'], timeout=10)
                        if img_response.status_code == 200:
                            # Fayl nomini yaratish
                            ext = found['image'].split('.')[-1].split('?')[0]
                            if ext not in ['jpg', 'jpeg', 'png', 'webp']:
                                ext = 'jpg'
                            filename = f"public/books/{book['id']}.{ext}"
                            
                            with open(filename, 'wb') as img_file:
                                img_file.write(img_response.content)
                            
                            book['local_image'] = f"/books/{book['id']}.{ext}"
                            print(f"  ✓ Rasm saqlandi: {filename}")
                    except Exception as e:
                        print(f"  ✗ Rasm yuklanmadi: {e}")
                
                print(f"  ✓ Topildi: {found.get('title')}")
            else:
                print(f"  ✗ Topilmadi")
        else:
            print(f"  ✗ API xatosi: {response.status_code}")
            
    except Exception as e:
        print(f"  ✗ Xato: {e}")
    
    updated_books.append(book)
    
    # Rate limit uchun kutish
    time.sleep(1)

# Yangilangan ma'lumotlarni saqlash
with open('public/books.json', 'w', encoding='utf-8') as f:
    json.dump(updated_books, f, ensure_ascii=False, indent=2)

print("\n✓ Barcha ma'lumotlar public/books.json ga saqlandi!")
