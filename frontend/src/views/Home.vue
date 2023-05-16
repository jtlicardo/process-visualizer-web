<template>
  <v-toolbar color="grey-lighten-4">
    <v-toolbar-title class="flex text-center"
      >PROCESS VISUALIZER</v-toolbar-title
    >
  </v-toolbar>
  <v-responsive class="d-flex align-center text-center fill-height">
    <OpenaiForm />
    <ProcessVisualizer />
  </v-responsive>
</template>

<script setup>
import ProcessVisualizer from "@/components/ProcessVisualizer.vue";
import OpenaiForm from "@/components/OpenaiForm.vue";
</script>
