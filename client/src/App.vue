<template lang="pug">
.app
  .status {{ status }}
</template>

<script lang="ts">
import { defineComponent, ref } from '@vue/composition-api';

const App = defineComponent({
  setup() {
    const status = ref('Please upload image');

    return {
      status,
    };
  },
});

export default App;
</script>

<style lang="scss">
*, *::before, *::after { @apply box-border m-0 p-0; }

.app {
  @apply flex justify-center items-center h-screen bg-center bg-cover;
  background-image: url('./assets/images/app_background.png');
}

// SETUP FONTS
@import url('https://fonts.googleapis.com/css2?family=Saira:wght@400;600&display=swap');
* { font-family: 'Saira', sans-serif; }

// SETUP PRIMARY AND SECONDARY COLOR HERE
:root {
  --color-primary-100: #ffdeb7;
  --color-primary-200: #ffc989;
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
