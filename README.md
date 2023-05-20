# Process visualizer - web app

This repository contains the web application for a tool designed to convert textual descriptions of processes into simplified BPMN (Business Process Model and Notation) diagrams. The web app builds upon the functionalities provided by the [process-visualizer](https://github.com/jtlicardo/process-visualizer) repository.

## Features

The web applications offers the following features:
* Textual process description input: Users can enter a textual description of a process directly into the web app.
* Process diagram visualization: The application uses NLP (Natural Language Processing) tools, including spaCy and a fine-tuned BERT model to extract key information from the text. It leverages OpenAI's models, such as `gpt-3.5-turbo`, to perform advanced tasks related to process description analysis. Please note that the availability of OpenAI's models may vary, and access to specific models, such as `gpt-4`, may require being on a waitlist or having access granted by OpenAI.
* Supported BPMN elements: The web app supports tasks, exclusive gateways, parallel gateways, start events, and end events.

## Prerequisites

Before running the web application, ensure that you have the following dependencies installed:

* [Docker](https://www.docker.com/get-started/): The web app is containerized using Docker, so Docker needs to be installed on your system.
* OpenAI API key: You need to have an OpenAI API key to utilize their models. If you don't have one, sign up on the [OpenAI website](https://openai.com/) and obtain an API key.

## How to run

To run the web application locally, follow these steps:
1. Clone this repository to your local machine.
1. Navigate to the cloned repository: `cd process-visualizer-web`
1. Start the application using Docker Compose: `docker-compose up -d --build`
1. Access the web app by opening your browser and navigating to `http://localhost:3000`

## Usage

1. Once you access the web application, you will be presented with a user-friendly interface.
1. Paste your OpenAI API key into the input field provided on the web page.
1. Enter the textual description of the process into the input field provided.
1. Click the "Submit" button to visualize the process.
1. The web app will analyze the input using NLP tools and OpenAI models, generating a simplified BPMN diagram.
1. The resulting diagram will be displayed on the web page, allowing you to visualize the process flow.
