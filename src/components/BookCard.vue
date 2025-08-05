<template>
  <div class="bg-gray-800 rounded-lg overflow-hidden transform hover:scale-105 transition duration-300 shadow-lg">
    <img :src="book.image" :alt="book.title" class="w-full h-48 sm:h-64 object-cover">
    <div class="p-4 sm:p-6">
      <h3 class="text-lg sm:text-2xl font-bold mb-2">{{ book.title }}</h3>
      <p class="text-gray-400 text-sm sm:text-base">{{ book.author }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BookCard',
  props: {
    book: {
      type: Object,
      required: true,
    },
  },
};
</script>
