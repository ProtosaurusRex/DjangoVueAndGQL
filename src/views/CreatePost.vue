<template>
  <div>
    <h2>Create a New Post ✏️</h2>
    <PostForm />
  </div>
</template>

<script>
import PostForm from '@/components/PostForm.vue'; // Adjust the path as necessary

export default {
  components: {
    PostForm,
  },
};
</script>