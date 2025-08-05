<template>
  <div class="bg-black text-white min-h-screen p-8">
    <h1 class="text-5xl font-bold mb-12 text-center">Siz uchun tavsiyalar</h1>

    <!-- Filtrlar -->
    <div class="flex justify-center items-center space-x-6 mb-12">
      <!-- Yosh tanlash -->
      <div class="relative">
        <select v-model="selectedAge" class="bg-gray-800 text-white font-bold py-3 px-6 rounded-full appearance-none focus:outline-none focus:ring-2 focus:ring-white">
          <option :value="null" disabled>Yoshingizni tanlang</option>
          <option value="7-10">7-10 yosh</option>
          <option value="11-15">11-15 yosh</option>
          <option value="16-20">16-20 yosh</option>
          <option value="21+">21+ yosh</option>
        </select>
      </div>

      <!-- Janrlar filteri -->
      <div class="relative">
        <select v-model="selectedGenre" class="bg-gray-800 text-white font-bold py-3 px-6 rounded-full appearance-none focus:outline-none focus:ring-2 focus:ring-white">
          <option value="">Barcha janrlar</option>
          <option v-for="genre in uniqueGenres" :key="genre" :value="genre">{{ genre }}</option>
        </select>
      </div>
    </div>

    <!-- Kitoblar ro'yxati -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <BookCard v-for="book in filteredBooks" :key="book.id" :book="book" />
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue';
import BookCard from '../components/BookCard.vue';

export default {
  name: 'Recommendations',
  components: {
    BookCard,
  },
  setup() {
    const books = ref([]);
    const selectedAge = ref(null);
    const selectedGenre = ref('');

    onMounted(async () => {
      const response = await fetch('/books.json');
      books.value = await response.json();
    });

    const uniqueGenres = computed(() => {
      return [...new Set(books.value.map(book => book.genre))];
    });

    const filteredBooks = computed(() => {
      let filtered = books.value;

      if (selectedAge.value) {
        filtered = filtered.filter(book => book.age_category === selectedAge.value);
      }

      if (selectedGenre.value) {
        filtered = filtered.filter(book => book.genre === selectedGenre.value);
      }

      return filtered;
    });

    return {
      books,
      selectedAge,
      selectedGenre,
      uniqueGenres,
      filteredBooks,
    };
  },
};
</script>