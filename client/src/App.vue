<template lang="pug">
.app Welcome to our Project
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
// .app {}

// SETUP PRIMARY AND SECONDARY COLOR HERE
:root {
  --color-primary-100: #E6FAF4;
  --color-primary-200: #BFF4E3;
  --color-primary-300: #99EDD3;
  --color-primary-400: #4DDFB1;
  --color-primary-500: #00D190;
  --color-primary-600: #00BC82;
  --color-primary-700: #007D56;
  --color-primary-800: #005E41;
  --color-primary-900: #003F2B;
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
