<template>
  <v-app-bar color="grey-lighten-4" :elevation="2">
    <v-app-bar-title class="flex text-center"
      >PROCESS VISUALIZER</v-app-bar-title
    >
  </v-app-bar>
  <v-responsive class="d-flex align-center text-center fill-height">
    <OpenaiForm @key-provided="displayAvailableModels" />
    <ProcessVisualizer :available-models="availableModels" />
  </v-responsive>
</template>

<script>
import ProcessVisualizer from "@/components/ProcessVisualizer.vue";
import OpenaiForm from "@/components/OpenaiForm.vue";

export default {
  components: {
    ProcessVisualizer,
    OpenaiForm,
  },
  data() {
    return {
      availableModels: [],
    };
  },
  methods: {
    displayAvailableModels(availableModels) {
      this.availableModels = availableModels;
    },
  },
};
</script>
