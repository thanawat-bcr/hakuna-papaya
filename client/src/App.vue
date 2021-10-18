<template lang="pug">
.app
  .title Hakuna Papaya
  .card.card-img
    .file-upload
      input(type="file" ref="fileInput")
    button.btn-upload(@click="$refs.fileInput.click()") Upload image of Papaya
  .card.card-status
    p.status(:class="{ 'opacity-50': status }") {{ result }}
</template>

<script lang="ts">
import { defineComponent, ref } from '@vue/composition-api';

const App = defineComponent({
  setup() {
    const result = ref('Please upload papaya...');
    const status = ref(true);

    const fileInput = ref(null);

    return {
      result,
      status,

      fileInput,
    };
  },
});

export default App;
</script>

<style lang="scss">
*, *::before, *::after { @apply box-border m-0 p-0; }

.app {
  @apply py-4 flex flex-col justify-center items-center h-screen bg-center bg-cover;
  background-image: url('./assets/images/app_background.png');
  .title { @apply font-bold text-4xl md:text-5xl; }
  .card {
    @apply my-4 flex flex-col justify-center items-center;
    width: 18rem;
    @media (min-width: 768px) { width: 22rem; }
    background: rgba(255, 255, 255, 0.6);
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 20px;
    &.card-img {
      @apply p-4;
      height: 26rem;
      input[type="file"] { @apply w-full h-full opacity-0 focus:outline-none cursor-pointer; }
      .file-upload {
        @apply mb-3 cursor-pointer relative transition;
        width: 16rem;
        height: 16rem;
        @media (min-width: 768px) { width: 20rem; height: 20rem; }

        // border: rgb(180, 180, 180) 2px dashed;
        border-radius: 0.5rem;
        background-color: rgba(37, 37, 37, 0.8);
        &:hover {
          background-color: rgba(37, 37, 37, 0.75);
        }
        &::before {
          content: '';
          @apply absolute w-44 h-44 bg-no-repeat bg-center bg-contain;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          background-image: url('./assets/images/photo.svg');
        }
      }
      .btn-upload {
        @apply w-full h-12 pl-8 bg-primary-300 rounded-xl text-white font-semibold text-lg relative;
        &:hover { @apply bg-primary-200; }
        &::after {
          content: '';
          @apply w-7 h-7 md:w-8 md:h-8 bg-contain bg-center bg-no-repeat absolute left-0;
          top: 50%;
          transform: translate(0.5rem, -50%);
          @media (min-width: 768px) { transform: translate(2rem, -50%); }
          background-image: url('./assets/images/photo.svg');
        }
      }
    }
    &.card-status {
      height: 5rem;
      p { @apply text-lg md:text-2xl; }
    }
  }
}

// SETUP FONTS
@import url('https://fonts.googleapis.com/css2?family=Saira:wght@400;600&display=swap');
* { font-family: 'Saira', sans-serif; }

// SETUP PRIMARY AND SECONDARY COLOR HERE
:root {
  --color-primary-100: #ffdeb7;
  --color-primary-200: #fac27d;
  --color-primary-300: #ffb35c;
  --color-primary-400: #fea33f;
  --color-primary-500: #fe932c;
  --color-primary-600: #f9882a;
  --color-primary-700: #f27828;
  --color-primary-800: #eb6925;
  --color-primary-900: #e14f21;
  --color-secondary-100: #E9EFF9;
  --color-secondary-200: #C7D7F1;
  --color-secondary-300: #A5BFE8;
  --color-secondary-400: #6290D7;
  --color-secondary-500: #1F60C6;
  --color-secondary-600: #1C56B2;
  --color-secondary-700: #133A77;
  --color-secondary-800: #0E2B59;
  --color-secondary-900: #091D3B;
}
</style>
