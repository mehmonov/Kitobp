<template>
  <div class="bg-black text-white min-h-screen flex flex-col items-center justify-center">
    <h1 class="text-6xl font-bold mb-8">Kitob Tavsiya Tizimi Kitob/p</h1>
    <p class="text-xl mb-12">Eng yaxshi kitoblarni toping</p>
    <router-link to="/recommendations">
      <button class="bg-white text-black font-bold py-4 px-8 rounded-full text-lg hover:bg-gray-200 transition duration-300">
        Tavsiya Olish
      </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>
