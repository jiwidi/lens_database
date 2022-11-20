<script setup></script>
<template>
  <div class="left">
    <h1>Lens Database header</h1>
  </div>
  <div class="container">

  <VTable :data="lenses">
    <template #head>
      <tr>
        <th>Name</th>
        <th>Mount</th>
      </tr>
    </template>
    <template #body="{rows}">
      <tr v-for="row in rows" :key="row.name">
        <td>{{ row.name }}</td>
        <td>{{ row.mount }}</td>
      </tr>
    </template>
  </VTable>
  </div>
</template>

<script>
import lenses from "./data/lenses.json";

export default {
  name: "main",
  data: () => ({
    lenses,
  }),
};
</script>

<style scoped></style>
