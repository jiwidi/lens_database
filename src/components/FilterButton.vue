<script setup>
import { ref } from 'vue'
let isActive = ref(false)

const emit = defineEmits(['updateFilter'])

function handleFilter() {
  isActive.value = !isActive.value
  emit('updateFilter', isActive.value ? 'add' : 'remove')
}
</script>

<template>
  <button :class="{ active : isActive }" @click="handleFilter">
    <slot />
  </button>
</template>
