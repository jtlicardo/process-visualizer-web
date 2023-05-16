<template>
  <v-container v-if="!keyProvided">
    <div class="background">
      <p class="mb-6">
        To use this app, please provide your <b>OpenAI API key</b>. <br />
        Your key will be used exclusively for the intended purposes of this app.
      </p>
      <v-form v-model="valid">
        <v-container>
          <v-row>
            <v-text-field
              v-model="apiKey"
              label="Paste your OpenAI API key here"
              required
            ></v-text-field>
          </v-row>
        </v-container>
      </v-form>
      <v-container>
        <v-btn
          class="mb-4"
          color="black"
          @click="submit"
          :loading="loading"
          :disabled="loading"
          >Submit key</v-btn
        >
      </v-container>
    </div>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      apiKey: "",
      keyProvided: false,
      loading: false,
      availableModels: [],
    };
  },
  methods: {
    async submit() {
      if (!this.apiKey) {
        alert("Please provide your OpenAI API key");
        return;
      }
      this.loading = true;
      try {
        let response = await axios.post(
          "http://localhost:5000/key",
          JSON.stringify({ key: this.apiKey }),
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        console.log(response);
        this.keyProvided = true;
        this.availableModels = response.data.available_models;
        this.$emit("key-provided", this.availableModels);
        alert("Key submitted successfully");
      } catch (e) {
        if (e.response.status === 401) {
          alert("Invalid OpenAI key");
        } else {
          alert("Something went wrong");
        }
        console.log(e);
      }
      this.loading = false;
    },
  },
};
</script>

<style scoped>
.background {
  background-color: #f5f5f5;
  width: 95%;
  padding: 2%;
  margin: 0 auto;
  border-radius: 8px;
}
</style>
