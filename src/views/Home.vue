<template>
  <v-responsive class="d-flex align-center text-center fill-height">
    <h1 class="my-10">Process visualizer</h1>
    <OpenaiForm />
    <ProcessVisualizer />
  </v-responsive>
</template>

<script setup>
import ProcessVisualizer from "@/components/ProcessVisualizer.vue";
import OpenaiForm from "@/components/OpenaiForm.vue";
</script>
