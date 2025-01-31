<template>
  <div>
    <template>
      <v-simple-table fixed-header id="header">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">User Name</th>
              <th class="text-left">Age</th>
              <th class="text-left">Veg / Non-veg</th>
              <th class="text-left">Weight</th>
              <th class="text-left">Height</th>
              <th class="text-left">BMI</th>
              <th class="text-left">Weight range</th>
              <th class="text-left">Diet Prediction</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="value in data" :key="value.id">
              <td>{{ value.user_name }}</td>
              <td>{{ value.age }}</td>
              <td>
                <div v-if="value.diet === true">Vegetarian</div>
                <div v-else>Non Vegetarian</div>
              </td>
              <td>{{ value.weight }}</td>
              <td>{{ value.height }}</td>
              <td>{{ value.bmi }}</td>
              <td>{{ value.body_type }}</td>
              <td>{{ value.nutrition_predict }}</td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </template>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
export default {
  data: () => ({
    firstName: "",
    lastName: "",
    email: "",
    data: "",
    token: Vue.$cookies.get("token"),
  }),

  mounted() {
    this.Submit();
  },

  methods: {
    Submit() {
      axios({
        method: "GET",
        url: "http://127.0.0.1:8000/get-nutrition/",
        data: JSON.stringify({}),
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Authorization: `token ${this.token}`,
        },
      })
        .then((res) => {
          this.data = res.data
          console.log(this.data);
        })
        .catch((error) => {
          alert(error);
          this.errored = true;
        });
    },
  },
};
</script>
