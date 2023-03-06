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
        :loading="loading"
        :disabled="loading"
        color="blue-lighten-5"
        @click="sendProcessDescription"
      >
        Submit
      </v-btn>
    </v-responsive>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      loading: false,
      processDescription: "",
    };
  },
  methods: {
    sendProcessDescription() {
      this.loading = true;
      const path = "http://localhost:5000/text";
      const data = {
        text: this.processDescription,
      };
      axios
        .post(path, JSON.stringify(data), {
          headers: {
            "Content-Type": "application/json",
          },
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
      this.loading = false;
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
