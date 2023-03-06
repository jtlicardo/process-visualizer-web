<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <h1 class="my-10">Process visualizer</h1>
      <v-textarea
        label="Process description"
        variant="outlined"
        v-model="processDescription"
      ></v-textarea>
      <v-btn
        :loading="loading[1]"
        :disabled="loading[1]"
        color="blue-lighten-5"
        @click="load(1)"
      >
        Submit
      </v-btn>
    </v-responsive>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      loading: [],
      processDescription: "",
    };
  },
  methods: {
    load(i) {
      this.loading[i] = true;
      setTimeout(() => (this.loading[i] = false), 3000);
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Open+Sans:wght@300&display=swap");

h1 {
  font-family: "Open Sans", sans-serif;
}
</style>
