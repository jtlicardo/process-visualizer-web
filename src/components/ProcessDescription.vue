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
        color="grey-lighten-4"
        @click="sendProcessDescription"
      >
        Submit
      </v-btn>
      <div v-if="imageUrl">
        <v-img
          :src="imageUrl"
          :width="imageWidth"
          class="my-14 mx-auto"
        ></v-img>
      </div>
    </v-responsive>
  </v-container>
</template>

<script>
import axios from "axios";
import { supabase } from "../supabase";

export default {
  data() {
    return {
      loading: false,
      imageUrl: null,
      imageWidth: 0,
      processDescription: "",
    };
  },
  methods: {
    async sendProcessDescription() {
      this.imageUrl = null;
      this.imageWidth = 0;
      this.loading = true;
      const path = "http://localhost:5000/text";
      let postData = {
        text: this.processDescription,
      };
      try {
        let response = await axios.post(path, JSON.stringify(postData), {
          headers: {
            "Content-Type": "application/json",
          },
        });
        let id = response.data.id;
        const { data } = supabase.storage
          .from("image-bucket")
          .getPublicUrl(`bpmn/${id}.jpeg`);
        this.imageUrl = data.publicUrl;
        // Check image width
        const img = new Image();
        img.src = this.imageUrl;
        img.onload = () => {
          this.imageWidth = img.naturalWidth;
        };
      } catch (e) {
        console.log(e);
      }
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
