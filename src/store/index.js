import { createStore } from 'vuex';
import { ApolloClient, createHttpLink, InMemoryCache, gql } from '@apollo/client/core';  // Import InMemoryCache here

const store = createStore({
  state() {
    return {
      user: null, // Store the user object or just userId
    };
  },
  mutations: {
    setUser(state, user) {
      state.user = user; // Set the user to the store
    },
  },
  actions: {
    // Define the action to get the current user using GraphQL
    async getCurrentUser({ commit }) {
      try {
        // GraphQL query to fetch the current user
        const GET_CURRENT_USER_QUERY = gql`
          query {
            currentUser {
              id
              name
              bio
              website
            }
          }
        `;

        // Perform the GraphQL query via Apollo Client
        const apolloClient = new ApolloClient({
          link: createHttpLink({ uri: 'http://localhost:8000/graphql/' }), // Set the URI to your GraphQL endpoint
          cache: new InMemoryCache(),  // Use InMemoryCache
        });

        const response = await apolloClient.query({
          query: GET_CURRENT_USER_QUERY,
        });

        const user = response.data.currentUser;

        // Check if we got a valid user and commit to the store
        if (user) {
          commit('setUser', user); // Save the user data to the store
        } else {
          throw new Error('No user data returned');
        }

        return user.id; // Return the user ID (or the entire user object if needed)
      } catch (error) {
        console.error('Error fetching user:', error);
        throw error; // Rethrow the error to handle it in the component
      }
    },
  },
  getters: {
    currentUser(state) {
      return state.user;
    },
  },
});

export default store;
