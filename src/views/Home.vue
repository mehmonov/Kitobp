<template>
  <div class="relative min-h-screen flex flex-col items-center justify-center text-white overflow-hidden">
    <!-- Orqa fon rasmi (kutubxonadagi talabalar) -->
    <div
      class="absolute inset-0 bg-cover bg-center scale-105"
      style="background-image: url('/hero-bg.jpg');"
    ></div>

    <!-- Matn o'qilishi uchun qoraytiruvchi gradient qatlam -->
    <div class="absolute inset-0 bg-gradient-to-b from-black/60 via-black/40 to-black/75"></div>

    <!-- Asosiy kontent -->
    <div class="relative z-10 flex flex-col items-center justify-center px-6 text-center max-w-3xl">
      <h1 class="text-4xl sm:text-6xl font-bold mb-6 drop-shadow-2xl leading-tight">
        Kitob Tavsiya Tizimi
      </h1>
      <p class="text-lg sm:text-2xl mb-10 text-gray-100 drop-shadow-lg">
        Yoshingiz va didingizga mos eng yaxshi kitoblarni toping
      </p>
      <router-link to="/recommendations">
        <button
          class="bg-white text-black font-bold py-4 px-10 rounded-full text-lg hover:bg-gray-200 hover:scale-105 transition duration-300 shadow-2xl"
        >
          Tavsiya Olish
        </button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
};
</script>
