// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '@/views/Dashboard.vue';
import Information from '@/views/Information.vue';
import Statistics from '@/views/Statistics.vue';
import StatisticsCourse from '@/views/StatisticsComponents/StatisticsCourse.vue';
import StatisticsStudent from '@/views/StatisticsComponents/StatisticsStudent.vue';
import StatisticsRepos from '@/views/StatisticsComponents/StatisticsRepos.vue';
import InformationCourse from '@/views/InformationComponents/InformationCourse.vue'
import InformationRepos from '@/views/InformationComponents/InformationRepos.vue'
import InformationStudent from '@/views/InformationComponents/InformationStudent.vue'
import QnA from '../views/QnA.vue'

const routes = [
  {
    path: '/board',
    name: 'board',
    component: Dashboard
  },
  {
    path: '/info',
    name: 'Information',
    component: Information,
    children: [
      { // default path
        path: '',
        redirect: '/info/course',
      },
      {
        path: 'course',
        name: 'InformationCourse',
        component: InformationCourse,
        props: true,
      },
      {
        path: 'students',
        name: 'InformationStudent',
        component: InformationStudent,
      },
      {
        path: 'repos',
        name: 'InformationRepos',
        component: InformationRepos,
      },
    ]
  },
  {
    path: '/statistics',
    name: 'Statistics',
    component: Statistics,
    children: [
      { // default path
        path: '',
        redirect: '/statistics/course',
      },
      {
        path: 'course',
        name: 'StatisticsCourse',
        component: StatisticsCourse,
        props: true,
      },
      {
        path: 'students',
        name: 'StatisticsStudent',
        component: StatisticsStudent,
      },
      {
        path: 'repos',
        name: 'StatisticsRepos',
        component: StatisticsRepos,
      },
    ]
  },
  {
    path: '/qna',
    name: 'QnA',
    component: QnA
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;