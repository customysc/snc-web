<template>
  <div class="tw:flex tw:flex-col tw:gap-4">
    <Banner/>
    <div class="tw:flex tw:flex-row tw:gap-4">
      <Announcement class="tw:flex-1"/>
      <HotTopics class="tw:flex-1"/>
    </div>
    <Cards />
  </div>
</template>

<script setup lang="ts">
import Banner from "@/components/views/home/Banner.vue";
import Cards from "@/components/views/home/Cards.vue";
import Announcement from "@/components/views/home/Announcement.vue";
import HotTopics from "@/components/views/home/HotTopics.vue";

</script>