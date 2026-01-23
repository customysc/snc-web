<template>
  <div class="tw:bg-[#bfdeff] tw:h-screen tw:w-full">
    {{ id }}
  </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()

const id = route.params.id
</script>
