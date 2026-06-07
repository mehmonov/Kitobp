<template>
  <div class="bg-black text-white min-h-screen p-4 sm:p-8">
    <!-- Orqaga tugma -->
    <router-link to="/" class="inline-block mb-6">
      <button class="text-gray-400 hover:text-white">← Orqaga</button>
    </router-link>

    <h1 class="text-3xl sm:text-4xl font-bold mb-8 text-center">Kitob Tavsiyalari</h1>

    <!-- Filtrlar -->
    <div class="flex flex-col sm:flex-row justify-center items-center gap-3 sm:gap-4 mb-8">
      <!-- Yosh tanlash -->
      <div class="relative w-full sm:w-60">
        <!-- chap ikona -->
        <svg class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
        </svg>
        <select
          v-model="selectedAge"
          style="color-scheme: dark;"
          class="appearance-none w-full bg-gray-800/70 border border-gray-700 text-white text-sm sm:text-base py-3 pl-11 pr-10 rounded-full cursor-pointer hover:bg-gray-700/70 hover:border-gray-600 focus:outline-none focus:ring-2 focus:ring-white/60 focus:border-transparent transition-colors duration-200"
        >
          <option value="" class="bg-gray-800 text-white">Barcha yoshlar</option>
          <option value="11-15" class="bg-gray-800 text-white">13-15 yosh</option>
          <option value="16-20" class="bg-gray-800 text-white">16+ yosh</option>
        </select>
        <!-- chevron -->
        <svg class="pointer-events-none absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke-width="2.2" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
        </svg>
      </div>

      <!-- Janr tanlash -->
      <div class="relative w-full sm:w-60">
        <!-- chap ikona -->
        <svg class="pointer-events-none absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke-width="1.7" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />
        </svg>
        <select
          v-model="selectedGenre"
          style="color-scheme: dark;"
          class="appearance-none w-full bg-gray-800/70 border border-gray-700 text-white text-sm sm:text-base py-3 pl-11 pr-10 rounded-full cursor-pointer hover:bg-gray-700/70 hover:border-gray-600 focus:outline-none focus:ring-2 focus:ring-white/60 focus:border-transparent transition-colors duration-200"
        >
          <option value="" class="bg-gray-800 text-white">Barcha janrlar</option>
          <option value="Jahon adabiyoti" class="bg-gray-800 text-white">Jahon adabiyoti</option>
          <option value="O'zbek adabiyoti" class="bg-gray-800 text-white">O'zbek adabiyoti</option>
        </select>
        <!-- chevron -->
        <svg class="pointer-events-none absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke-width="2.2" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
        </svg>
      </div>
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
