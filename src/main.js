import "./assets/main.css";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { ApolloClient, createHttpLink, InMemoryCache } from "@apollo/client/core";
import { provideApolloClient } from "@vue/apollo-composable"; // Import provideApolloClient
import CreatePost from './views/CreatePost.vue';
import store from './store';

const httpLink = createHttpLink({
  uri: "http://localhost:8000/graphql/", // Update your endpoint if needed
});

const cache = new InMemoryCache();

const apolloClient = new ApolloClient({
  link: httpLink,
  cache,
});

// Create the app instance
const app = createApp(App);

// Provide the Apollo client to the entire app
provideApolloClient(apolloClient); // This is the critical line to provide Apollo Client

// Register the CreatePost component globally
app.component('CreatePost', CreatePost);

// Use the router and store
app.use(router);
app.use(store);

// Mount the app
app.mount("#app");
