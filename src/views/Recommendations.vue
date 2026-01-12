<template>
  <div class="bg-black text-white min-h-screen p-4 sm:p-8">
    <!-- Orqaga tugma -->
    <router-link to="/" class="inline-block mb-6">
      <button class="text-gray-400 hover:text-white">← Orqaga</button>
    </router-link>

    <h1 class="text-3xl sm:text-4xl font-bold mb-8 text-center">Kitob Tavsiyalari</h1>

    <!-- Filtrlar -->
    <div class="flex flex-col sm:flex-row justify-center items-center gap-4 mb-8">
      <!-- Yosh tanlash -->
      <select 
        v-model="selectedAge" 
        class="bg-gray-800 text-white py-3 px-6 rounded-full focus:outline-none focus:ring-2 focus:ring-white w-full sm:w-auto"
      >
        <option value="">Barcha yoshlar</option>
        <option value="11-15">13-15 yosh</option>
        <option value="16-20">16+ yosh</option>
      </select>

      <!-- Janr tanlash -->
      <select 
        v-model="selectedGenre" 
        class="bg-gray-800 text-white py-3 px-6 rounded-full focus:outline-none focus:ring-2 focus:ring-white w-full sm:w-auto"
      >
        <option value="">Barcha janrlar</option>
        <option value="Jahon adabiyoti">Jahon adabiyoti</option>
        <option value="O'zbek adabiyoti">O'zbek adabiyoti</option>
      </select>
    </div>

    <!-- Natijalar soni -->
    <p class="text-center text-gray-400 mb-6">{{ filteredBooks.length }} ta kitob topildi</p>

    <!-- Kitoblar ro'yxati -->
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 sm:gap-6">
      <BookCard v-for="book in filteredBooks" :key="book.id" :book="book" />
    </div>

    <!-- Bo'sh holat -->
    <div v-if="filteredBooks.length === 0" class="text-center text-gray-400 py-12">
      Kitob topilmadi. Filtrlarni o'zgartiring.
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
    const selectedAge = ref('');
    const selectedGenre = ref('');

    onMounted(async () => {
      const response = await fetch('/books.json');
      books.value = await response.json();
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
      filteredBooks,
    };
  },
};
</script>
