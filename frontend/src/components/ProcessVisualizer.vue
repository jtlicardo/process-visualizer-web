<template>
  <v-container>
    <p class="my-6"><b>OpenAI model to use</b></p>
    <v-select
      v-model="selectedModel"
      label="Select"
      :items="availableModels"
    ></v-select>
  </v-container>
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
      <p>{{ currentStatus }}</p>
      <div v-if="imageCreated">
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

export default {
  props: {
    availableModels: {
      type: Array,
      required: true,
      default: () => [],
    },
  },
  data() {
    return {
      selectedModel: null,
      processDescription: "",
      loading: false,
      imageCreated: null,
      imageWidth: 0,
      currentStatus: "",
      imageUrl: null,
    };
  },
  methods: {
    onImageCreated() {
      this.imageUrl = new URL(
        "../assets/generated_images/bpmn.jpeg",
        import.meta.url
      ).href;
      const img = new Image();
      img.src = this.imageUrl;
      img.onload = () => {
        this.imageWidth = img.width;
      };
      this.imageCreated = true;
    },
    loadExample(num) {
      if (num === 1) {
        this.processDescription =
          "The process begins when the student logs in to the university's website. He then takes an online exam. After that, " +
          "the system grades it. If the student scores below 60%, he takes the exam again. If the student scores 60% or higher " +
          "on the exam, the professor enters the grade.";
      } else if (num === 2) {
        this.processDescription =
          "The customer decides if he wants to finance or pay in cash. If the customer chooses to finance, " +
          "the customer will need to fill out a loan application. After that, the customer sends the application to the bank. If the " +
          "customer chooses to pay in cash, the customer will need to bring the total cost of the car to the dealership in order to " +
          "complete the transaction. After the customer has chosen to finance or pay in cash, the customer must sign the contract before " +
          "the transaction is completed.";
      } else if (num === 3) {
        this.processDescription =
          "The process starts when the R&D team generates ideas for new products. At this point, 3 things occur in " +
          "parallel: the first thing is the engineering team analyzing the ideas for feasibility. The engineering team also creates the technical " +
          "specification. The second path involves the marketing team conducting market research for the ideas. At the same time, the design team " +
          "creates visual concepts for the potential products. The third path sees the financial analysts reviewing the potential cost of the ideas. " +
          "Once each track has completed its analysis, the management reviews the findings of the analysis.";
      }
    },
    initializeEventSource() {
      console.log("Initializing event source");
      const eventSource = new EventSource("http://localhost:5000/stream");
      eventSource.onmessage = (event) => {
        var data = JSON.parse(event.data);
        this.currentStatus = data.message;
      };
    },
    async sendProcessDescription() {
      if (!this.selectedModel) {
        alert("Please select a model");
        return;
      }
      this.imageCreated = false;
      this.loading = true;
      try {
        this.currentStatus = "Starting process...";
        this.initializeEventSource();
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
