<template>
    <div>
      <h3>Fill out the form below:</h3>
      <form @submit.prevent="submitPost">
        <div>
          <label for="title">Title:</label>
          <input type="text" v-model="post.title" required />
        </div>
        <div>
          <label for="body">Content:</label>
          <textarea v-model="post.body" required></textarea>
        </div>
        <div>
          <label for="tags">Tags (comma-separated):</label>
          <input type="text" v-model="tagsInput" />
        </div>
        <button type="submit">Submit</button>
        <div v-if="error" class="error">{{ error }}</div>
      </form>
    </div>
  </template>
  
  <script>
  import { gql } from '@apollo/client/core'; // Use the Apollo client from core
  import { useMutation } from '@vue/apollo-composable'; // Use Apollo's Vue 3 composable functions
  import { mapActions } from 'vuex';
  
  export default {
    data() {
      return {
        post: {
          title: '',
          body: '',
        },
        tagsInput: '',
        error: null,
      };
    },
    methods: {
      ...mapActions(['getCurrentUser']), // Import the action from Vuex
  
      async submitPost() {
        try {
          const authorId = await this.getCurrentUser(); // Get current user's profile ID
  
          const tags = this.tagsInput.split(',').map(tag => ({ name: tag.trim() }));
  
          // Define the mutation
          const CREATE_POST_MUTATION = gql`
            mutation CreatePost($input: CreatePostInput!) {
              createPost(input: $input) {
                post {
                  id
                  title
                  body
                }
                errors
              }
            }
          `;
  
          // Call the useMutation hook
          const { mutate, onError, onDone } = useMutation(CREATE_POST_MUTATION);
  
          // Execute the mutation
          const response = await mutate({
            input: {
              title: this.post.title,
              body: this.post.body,
              authorId: authorId, // Use the retrieved authorId
              tags: tags,
            },
          });
  
          // Handle the response
          const { data } = response;
          if (data.createPost.errors) {
            this.error = data.createPost.errors.join(', ');
          } else {
            console.log('Post created:', data.createPost.post);
            this.resetForm(); // Clear the form
          }
        } catch (error) {
          console.error('Error creating post:', error);
          this.error = 'Failed to create post. Please try again.';
        }
      },
  
      resetForm() {
        this.post.title = '';
        this.post.body = '';
        this.tagsInput = '';
        this.error = null;
      },
    },
  };
  </script>
  
  <style scoped>
  .error {
    color: red;
  }
  </style>
  