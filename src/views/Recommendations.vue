<template>
  <div class="bg-black text-white min-h-screen p-8">
    <h1 class="text-5xl font-bold mb-12 text-center">Siz uchun tavsiyalar</h1>

    <!-- Yosh tanlash -->
    <div class="mb-12">
      <h2 class="text-3xl font-bold mb-6 text-center">Yoshingizni tanlang</h2>
      <div class="flex justify-center space-x-4">
        <button @click="selectAge('7-15')" :class="{'bg-white text-black': selectedAge === '7-15'}" class="bg-gray-800 text-white font-bold py-3 px-6 rounded-full text-lg hover:bg-white hover:text-black transition duration-300">7-15 yosh</button>
        <button @click="selectAge('16+')" :class="{'bg-white text-black': selectedAge === '16+'}" class="bg-gray-800 text-white font-bold py-3 px-6 rounded-full text-lg hover:bg-white hover:text-black transition duration-300">16+ yosh</button>
      </div>
    </div>

    <!-- Janrlar filteri -->
    <div v-if="selectedAge" class="mb-12">
      <h2 class="text-3xl font-bold mb-6 text-center">Janrni tanlang</h2>
      <div class="flex justify-center flex-wrap gap-4">
        <button v-for="genre in uniqueGenres" :key="genre" @click="toggleGenre(genre)" :class="{'bg-white text-black': selectedGenres.includes(genre)}" class="bg-gray-800 text-white font-bold py-2 px-4 rounded-full hover:bg-white hover:text-black transition duration-300">{{ genre }}</button>
      </div>
    </div>

    <!-- Kitoblar ro'yxati -->
    <div v-if="selectedAge" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
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
    const selectedGenres = ref([]);

    onMounted(async () => {
      const response = await fetch('/books.json');
      books.value = await response.json();
    });

    const selectAge = (age) => {
      selectedAge.value = age;
      selectedGenres.value = [];
    };

    const toggleGenre = (genre) => {
      const index = selectedGenres.value.indexOf(genre);
      if (index === -1) {
        selectedGenres.value.push(genre);
      } else {
        selectedGenres.value.splice(index, 1);
      }
    };

    const uniqueGenres = computed(() => {
      if (!selectedAge.value) return [];
      const ageFilteredBooks = books.value.filter(book => book.age_category === selectedAge.value);
      return [...new Set(ageFilteredBooks.map(book => book.genre))];
    });

    const filteredBooks = computed(() => {
      if (!selectedAge.value) return [];
      let ageFilteredBooks = books.value.filter(book => book.age_category === selectedAge.value);
      if (selectedGenres.value.length === 0) {
        return ageFilteredBooks;
      }
      return ageFilteredBooks.filter(book => selectedGenres.value.includes(book.genre));
    });

    return {
      books,
      selectedAge,
      selectedGenres,
      selectAge,
      toggleGenre,
      uniqueGenres,
      filteredBooks,
    };
  },
};
</script>