<template>
  <div class="background">
    <p class="mb-6">
      To use this app, please provide your OpenAI API key. Your key will be used
      exclusively for the intended purposes of this app. <br />
      For security reasons, we recommend that you delete your API key as soon as
      you are done using this app.
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
      <v-btn class="mb-4" color="black" @click="submit">Submit key</v-btn>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      apiKey: "",
    };
  },
  methods: {
    submit() {},
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
