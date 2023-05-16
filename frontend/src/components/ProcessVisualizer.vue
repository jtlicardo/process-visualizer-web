<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <v-container>
        <v-btn class="mx-2 mb-4" color="grey-lighten-4" @click="loadExample(1)"
          >Example #1</v-btn
        >
        <v-btn class="mx-2 mb-4" color="grey-lighten-4" @click="loadExample(2)"
          >Example #2</v-btn
        >
        <v-btn class="mx-2 mb-4" color="grey-lighten-4" @click="loadExample(3)"
          >Example #3</v-btn
        >
      </v-container>
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
        class="mb-2"
      >
        Submit
      </v-btn>
      <div v-if="imageCreated">
        <v-img :src="imageUrl" class="my-14 mx-auto"></v-img>
      </div>
    </v-responsive>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      processDescription: "",
      loading: false,
      imageCreated: null,
      imageCreatedTimestamp: 0,
    };
  },
  computed: {
    imageUrl() {
      return `/generated_images/bpmn.jpeg?timestamp=${this.imageCreatedTimestamp}`;
    },
  },
  methods: {
    onImageCreated() {
      this.imageCreated = true;
      this.imageCreatedTimestamp = Date.now();
    },
    loadExample(num) {
      if (num === 1) {
        this.processDescription =
          "The customer fills out a loan application. Meanwhile, the manager decides " +
          "whether to prepare additional questions. If yes, the manager prepares additional questions. If the " +
          "decision is not to prepare, the manager waits for the customer. After all those activities are finished, " +
          "the customer sends the application.";
      } else if (num === 2) {
        this.processDescription =
          "The first step is for the student to register for the exam through the university's " +
          "online portal. Once registered, he will receive an email confirming their registration. Next, he will need to " +
          "arrive at the exam location on the day of the exam. Before entering the exam room, the student will be required " +
          "to check in with an exam administrator. Once inside the exam room, the student will take the exam. Once the exam " +
          "time is up, the student will need to submit their completed exam. He will then be allowed to leave the exam room. " +
          "After the exam, the professor will grade the exams. The students will receive their exam results at a later date.";
      } else if (num === 3) {
        this.processDescription =
          "The process begins with the student choosing his preferences. The professor then saves " +
          "the preferences to a database. He then allocates the student. After that, he informs the employer and the student " +
          "about the allocation. The employer evaluates the candidate. If the student is not accepted, the employer informs the " +
          "student. Ater that the student chooses his preferences again. If the student is accepted, he completes the internship. " +
          "After the student has done that, the professor updates the database.";
      }
    },
    async sendProcessDescription() {
      this.imageCreated = false;
      this.loading = true;
      try {
        let response = await axios.post(
          "http://localhost:5000/text",
          JSON.stringify({
            text: this.processDescription,
          }),
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        console.log(response);
        this.onImageCreated();
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
