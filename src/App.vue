<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div id="app">
      <h1>My Blog 🦖</h1>
      <nav>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/create-post">New Post</RouterLink>
        <RouterLink to="/">Posts</RouterLink>
      </nav>
    </div>
  </header>

  <!-- This will render the matched component for each route -->
  <RouterView />
</template>

<style scoped>
h1 {
  text-align: center;
  font-weight: bold;
  margin-bottom: 1rem;
}

header {
  border-bottom: 1px solid #ccc;
  margin-bottom: 1rem;
}

nav {
  text-align: center;
  margin: 1rem 0;
}

nav a {
  padding: 0.5rem;
}
</style>

