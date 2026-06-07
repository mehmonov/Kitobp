<template>
  <div>
    <!-- Kitob kartasi -->
    <div 
      @click="openModal" 
      class="bg-gray-800 rounded-lg overflow-hidden transform hover:scale-105 transition duration-300 shadow-lg cursor-pointer"
    >
      <img 
        v-if="book.local_image || book.image" 
        :src="book.local_image || book.image" 
        :alt="book.title" 
        class="w-full h-48 sm:h-64 object-cover"
      >
      <div v-else class="w-full h-48 sm:h-64 bg-gray-700 flex items-center justify-center">
        <span class="text-4xl">📚</span>
      </div>
      <div class="p-4">
        <h3 class="text-base sm:text-lg font-bold mb-1 line-clamp-2">{{ book.title }}</h3>
        <p class="text-gray-400 text-sm">{{ book.author }}</p>
      </div>
    </div>

    <!-- Modal -->
    <div 
      v-if="showModal" 
      class="fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center z-50 p-4"
      @click.self="closeModal"
    >
      <div class="bg-gray-900 rounded-lg max-w-lg w-full max-h-[90vh] overflow-y-auto">
        <div class="p-6">
          <button @click="closeModal" class="float-right text-gray-400 hover:text-white text-2xl">&times;</button>
          
          <img 
            v-if="book.local_image || book.image" 
            :src="book.local_image || book.image" 
            :alt="book.title" 
            class="w-full h-64 object-cover rounded-lg mb-4"
          >
          <div v-else class="w-full h-64 bg-gray-700 flex items-center justify-center rounded-lg mb-4">
            <span class="text-6xl">📚</span>
          </div>
          
          <h2 class="text-2xl font-bold mb-2">{{ book.api_title || book.title }}</h2>
          <p class="text-gray-400 mb-4">{{ book.author }}</p>
          
          <p v-if="book.description" class="text-gray-300 mb-4 text-sm leading-relaxed">
            {{ book.description }}
          </p>
          <p v-else class="text-gray-500 mb-4 text-sm">
            Bu kitob haqida ma'lumot mavjud emas.
          </p>
          
          <a 
            v-if="officialLink"
            :href="officialLink" 
            target="_blank"
            rel="noopener noreferrer"
            class="inline-block bg-white text-black font-bold py-3 px-6 rounded-full hover:bg-gray-200 transition duration-300"
          >
            {{ officialLinkLabel }}
          </a>
          <p v-if="book.official_link_note" class="mt-2 text-xs leading-relaxed text-gray-500">
            {{ book.official_link_note }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, ref } from 'vue';

export default {
  name: 'BookCard',
  props: {
    book: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const showModal = ref(false);
    const officialLink = computed(() => {
      if (props.book.official_link_url) return props.book.official_link_url;
      if (props.book.slug) return `https://mutolaa.com/uz/book/${props.book.slug}`;
      return '';
    });
    const officialLinkLabel = computed(() => (
      props.book.official_link_label || "Onlayn o'qish"
    ));

    const openModal = () => {
      showModal.value = true;
      document.body.style.overflow = 'hidden';
    };

    const closeModal = () => {
      showModal.value = false;
      document.body.style.overflow = '';
    };

    return {
      showModal,
      officialLink,
      officialLinkLabel,
      openModal,
      closeModal
    };
  },
};
</script>
