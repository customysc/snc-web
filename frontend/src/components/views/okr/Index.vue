<template>
  <div style="width: 100vw; height: 100vh; display: flex; background-color: #F5F7FA; overflow: hidden; margin: 0; padding: 0; position: fixed; top: 0; left: 0; right: 0; bottom: 0;">
    <div style="width: 200px; background: linear-gradient(180deg, #409EFF 0%, #66B1FF 100%); display: flex; flex-direction: column; box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1); z-index: 10; flex-shrink: 0;">
      <div style="padding: 16px; border-bottom: 1px solid rgba(255, 255, 255, 0.2);">
        <div style="display: flex; align-items: center; gap: 8px;">
          <el-avatar :size="36" :src="currentUser.avatar" style="border: 2px solid rgba(255, 255, 255, 0.8);" />
          <div>
            <div style="font-size: 14px; font-weight: 600; color: #FFFFFF;">{{ currentUser.name }}</div>
            <div style="font-size: 10px; color: rgba(255, 255, 255, 0.8);">OKR 管理中心</div>
          </div>
        </div>
      </div>

      <div style="flex: 1; overflow-y: auto; padding: 12px 0;">
        <div style="padding: 0 12px; margin-bottom: 16px;">
          <div style="display: flex; align-items: center; gap: 4px; margin-bottom: 8px; padding: 0 4px;">
            <el-icon style="color: #FFFFFF; font-size: 14px;"><UserFilled /></el-icon>
            <span style="font-size: 12px; font-weight: 600; color: #FFFFFF;">我的 OKR</span>
          </div>
          <div @click="viewMyOkrs"
               :style="{
                 display: 'flex',
                 alignItems: 'center',
                 gap: '8px',
                 padding: '8px 12px',
                 borderRadius: '4px',
                 cursor: 'pointer',
                 transition: 'all 0.3s',
                 backgroundColor: viewingMyOkrs ? 'rgba(255, 255, 255, 0.25)' : 'transparent',
                 border: viewingMyOkrs ? '1px solid rgba(255, 255, 255, 0.5)' : '1px solid transparent'
               }">
            <el-avatar :size="28" :src="currentUser.avatar" />
            <div style="flex: 1;">
              <div style="font-size: 12px; font-weight: 500; color: #FFFFFF;">{{ currentUser.name }}</div>
              <div style="font-size: 10px; color: rgba(255, 255, 255, 0.7);">查看我的目标</div>
            </div>
            <el-icon v-if="viewingMyOkrs" style="color: #FFFFFF; font-size: 12px;"><Check /></el-icon>
          </div>
        </div>

        <div style="padding: 0 12px; margin-bottom: 16px;">
          <div style="display: flex; align-items: center; gap: 4px; margin-bottom: 8px; padding: 0 4px;">
            <el-icon style="color: #FFFFFF; font-size: 14px;"><User /></el-icon>
            <span style="font-size: 12px; font-weight: 600; color: #FFFFFF;">管理的成员</span>
          </div>
          <div v-for="member in managedMembers" :key="member.id" 
               @click="selectMember(member)"
               :style="{
                 display: 'flex',
                 alignItems: 'center',
                 gap: '8px',
                 padding: '8px 12px',
                 borderRadius: '4px',
                 cursor: 'pointer',
                 transition: 'all 0.3s',
                 backgroundColor: selectedMember?.id === member.id ? 'rgba(255, 255, 255, 0.25)' : 'transparent',
                 border: selectedMember?.id === member.id ? '1px solid rgba(255, 255, 255, 0.5)' : '1px solid transparent'
               }">
            <el-avatar :size="28" :src="member.avatar" />
            <div style="flex: 1;">
              <div style="font-size: 12px; font-weight: 500; color: #FFFFFF;">{{ member.name }}</div>
              <div style="font-size: 10px; color: rgba(255, 255, 255, 0.7);">
                {{ member.department }}
                {{ member.major ? ' · ' + member.major : '' }}
                {{ member.grade ? ' · ' + member.grade : '' }}
                {{ member.role ? ' · ' + member.role : '' }}
              </div>
            </div>
            <el-icon 
              @click.stop="toggleFollow(member)"
              :style="{
                color: isFollowed(member.id) ? '#FFD700' : 'rgba(255, 255, 255, 0.5)',
                fontSize: '16px',
                cursor: 'pointer',
                transition: 'all 0.3s'
              }"
              :title="isFollowed(member.id) ? '取消关注' : '关注'"
            >
              <Star :fill="isFollowed(member.id) ? '#FFD700' : 'none'" />
            </el-icon>
            <el-icon v-if="selectedMember?.id === member.id" style="color: #FFFFFF; font-size: 12px;"><Check /></el-icon>
          </div>
        </div>

        <div style="padding: 0 12px; margin-bottom: 16px;">
          <div style="display: flex; align-items: center; gap: 4px; margin-bottom: 8px; padding: 0 4px;">
            <el-icon style="color: #FFFFFF; font-size: 14px;"><Star /></el-icon>
            <span style="font-size: 12px; font-weight: 600; color: #FFFFFF;">关注的人</span>
          </div>
          <div v-if="followedMembers.length === 0" style="padding: 12px; text-align: center; color: rgba(255, 255, 255, 0.5); font-size: 11px;">
            暂无关注的人
          </div>
          <div v-for="member in followedMembers" :key="member.id"
               @click="selectMember(member)"
               :style="{
                 display: 'flex',
                 alignItems: 'center',
                 gap: '8px',
                 padding: '8px 12px',
                 borderRadius: '4px',
                 cursor: 'pointer',
                 transition: 'all 0.3s',
                 backgroundColor: selectedMember?.id === member.id ? 'rgba(255, 255, 255, 0.25)' : 'transparent',
                 border: selectedMember?.id === member.id ? '1px solid rgba(255, 255, 255, 0.5)' : '1px solid transparent'
               }">
            <el-avatar :size="28" :src="member.avatar" />
            <div style="flex: 1;">
              <div style="font-size: 12px; font-weight: 500; color: #FFFFFF;">{{ member.name }}</div>
              <div style="font-size: 10px; color: rgba(255, 255, 255, 0.7);">
                {{ member.department }}
                {{ member.major ? ' · ' + member.major : '' }}
                {{ member.grade ? ' · ' + member.grade : '' }}
                {{ member.role ? ' · ' + member.role : '' }}
              </div>
            </div>
            <el-icon v-if="selectedMember?.id === member.id" style="color: #FFFFFF; font-size: 12px;"><Check /></el-icon>
          </div>
        </div>
      </div>

      <div style="padding: 12px; border-top: 1px solid rgba(255, 255, 255, 0.2);">
        <div @click="viewAllOkrs"
             :style="{
               display: 'flex',
               alignItems: 'center',
               justifyContent: 'center',
               gap: '4px',
               padding: '8px',
               borderRadius: '4px',
               cursor: 'pointer',
               transition: 'all 0.3s',
               backgroundColor: !selectedMember && !viewingMyOkrs ? 'rgba(255, 255, 255, 0.25)' : 'transparent',
               border: !selectedMember && !viewingMyOkrs ? '1px solid rgba(255, 255, 255, 0.5)' : '1px solid transparent'
             }">
          <el-icon style="color: #FFFFFF; font-size: 14px;"><List /></el-icon>
          <span style="font-size: 12px; font-weight: 500; color: #FFFFFF;">查看全部 OKR</span>
        </div>
      </div>
    </div>

    <div style="flex: 1; display: flex; flex-direction: column; overflow: hidden;">
      <div style="padding: 20px 24px; background-color: #FFFFFF; border-bottom: 1px solid #E4E7ED; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); flex-shrink: 0;">
        <h2 style="margin: 0; font-size: 24px; font-weight: 600; color: #303133;">
          {{ viewingMyOkrs ? '我的 OKR' : (selectedMember ? `${selectedMember.name} 的 OKR` : 'OKR 目标管理') }}
        </h2>
        <p style="margin: 6px 0 0 0; font-size: 14px; color: #909399;">
          {{ viewingMyOkrs ? '查看和管理我的目标与关键结果' : (selectedMember ? `${selectedMember.department} ${selectedMember.position ? '· ' + selectedMember.position : ''}` : '查看和管理团队的目标与关键结果') }}
        </p>
      </div>

      <div ref="scrollContainer" style="flex: 1; overflow-y: auto; padding: 20px; overflow-x: hidden; width: 100%; box-sizing: border-box;">
        <div style="width: 100%; max-width: none; box-sizing: border-box;">
          <div v-if="filteredOkrList.length === 0" style="text-align: center; padding: 60px 30px; background-color: #FFFFFF; border-radius: 8px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);">
            <el-empty description="暂无OKR数据" />
          </div>

          <div v-else>
            <OkrCard 
        v-for="okr in filteredOkrList" 
        :key="okr.id"
        :objective="okr.objective"
        :owner="okr.owner"
        :owner-id="okr.ownerId"
        :participants="okr.participants"
        :keyResults="okr.keyResults"
        :totalScore="okr.totalScore"
        :created-date="okr.createdDate"
        :is-followed="isFollowed"
        :toggle-follow="toggleFollowById"
        @select-participant="handleSelectParticipant"
      />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import OkrCard from './OkrCard.vue';
import { ElMessage } from 'element-plus';
// @ts-ignore
import { okrData, currentUser, managedMembers, followingMembers } from './mockData.js';
import { Star, List, Check, UserFilled } from '@element-plus/icons-vue';

interface IndexSubTask {
  id: number;
  title: string;
  progress: number;
}

interface IndexTask {
  id: number;
  title: string;
  progress: number;
  subtasks: IndexSubTask[];
}

interface IndexParticipant {
  id: number;
  name: string;
  avatar: string;
  role: string;
  tasks?: IndexTask[];
}

interface Member {
  id: number;
  name: string;
  avatar: string;
  department: string;
  position?: string;
  major?: string;
  grade?: string;
  role?: string;
}

interface IndexKeyResult {
  id: number;
  title: string;
  progress: number;
  weight: number;
  score: number;
  status: 'normal' | 'risk' | 'delayed';
}

interface OkrData {
  id: number;
  objective: string;
  owner: string;
  ownerId: number;
  participants: IndexParticipant[];
  keyResults: IndexKeyResult[];
  totalProgress: number;
  totalScore: number;
  createdDate?: string;
}

const selectedMember = ref<Member | null>(null);
const viewingMyOkrs = ref(true);
const okrList = ref<OkrData[]>([]);
const followedMemberIds = ref<number[]>([]);
const scrollContainer = ref<HTMLElement | null>(null);

const followedMembers = computed(() => {
  const allMembers = [...managedMembers, ...followingMembers] as Member[];
  return allMembers.filter(m => followedMemberIds.value.includes(m.id));
});

const toggleFollow = (member: Member) => {
  const index = followedMemberIds.value.indexOf(member.id);
  if (index > -1) {
    followedMemberIds.value.splice(index, 1);
    ElMessage.success(`已取消关注 ${member.name}`);
  } else {
    followedMemberIds.value.push(member.id);
    ElMessage.success(`关注成功！`);
  }
};

const toggleFollowById = (memberId: number, memberName: string) => {
  const index = followedMemberIds.value.indexOf(memberId);
  if (index > -1) {
    followedMemberIds.value.splice(index, 1);
    ElMessage.success(`已取消关注 ${memberName}`);
  } else {
    followedMemberIds.value.push(memberId);
    ElMessage.success(`关注成功！`);
  }
};

const isFollowed = (memberId: number) => {
  return followedMemberIds.value.includes(memberId);
};

const filteredOkrList = computed(() => {
  if (viewingMyOkrs.value) {
    const myOkrList: OkrData[] = [];
    okrList.value.forEach(okr => {
      if (okr.ownerId === currentUser.id) {
        myOkrList.push(okr);
      } else {
        const participant = okr.participants.find(p => p.id === currentUser.id);
        if (participant && participant.tasks) {
          participant.tasks.forEach(task => {
            const taskKeyResults = task.subtasks.map(subtask => ({
              id: subtask.id,
              title: subtask.title,
              progress: subtask.progress,
              weight: Math.round(100 / task.subtasks.length),
              score: parseFloat((subtask.progress / 20).toFixed(1))
            }));
            
            const taskTotalProgress = task.subtasks.length > 0 
              ? Math.round(task.subtasks.reduce((sum, st) => sum + st.progress, 0) / task.subtasks.length)
              : task.progress;
            
            const taskTotalScore = taskKeyResults.length > 0
              ? parseFloat((taskKeyResults.reduce((sum, kr) => sum + kr.score, 0) / taskKeyResults.length).toFixed(1))
              : parseFloat((task.progress / 20).toFixed(1));
            
            myOkrList.push({
              id: okr.id * 1000 + task.id,
              objective: task.title,
              owner: currentUser.name,
              ownerId: currentUser.id,
              participants: [
                {
                  id: currentUser.id,
                  name: currentUser.name,
                  avatar: currentUser.avatar,
                  role: participant.role,
                  tasks: [{
                    id: task.id,
                    title: task.title,
                    progress: task.progress,
                    subtasks: task.subtasks
                  }]
                }
              ],
              keyResults: taskKeyResults,
              totalProgress: taskTotalProgress,
              totalScore: taskTotalScore,
              createdDate: okr.createdDate
            });
          });
        }
      }
    });
    return myOkrList;
  }
  if (selectedMember.value) {
    const memberOkrList = okrList.value.filter(okr => {
      return okr.ownerId === selectedMember.value!.id || 
             okr.participants.some(p => p.id === selectedMember.value!.id);
    });
    
    if (selectedMember.value.id === currentUser.id) {
      const currentUserOkrList: OkrData[] = [];
      memberOkrList.forEach(okr => {
        if (okr.ownerId === currentUser.id) {
          currentUserOkrList.push(okr);
        } else {
          const participant = okr.participants.find(p => p.id === currentUser.id);
          if (participant && participant.tasks) {
            participant.tasks.forEach(task => {
              const taskKeyResults = task.subtasks.map(subtask => ({
                id: subtask.id,
                title: subtask.title,
                progress: subtask.progress,
                weight: Math.round(100 / task.subtasks.length),
                score: parseFloat((subtask.progress / 20).toFixed(1))
              }));
              
              const taskTotalProgress = task.subtasks.length > 0 
                ? Math.round(task.subtasks.reduce((sum, st) => sum + st.progress, 0) / task.subtasks.length)
                : task.progress;
              
              const taskTotalScore = taskKeyResults.length > 0
                ? parseFloat((taskKeyResults.reduce((sum, kr) => sum + kr.score, 0) / taskKeyResults.length).toFixed(1))
                : parseFloat((task.progress / 20).toFixed(1));
              
              currentUserOkrList.push({
                id: okr.id * 1000 + task.id,
                objective: task.title,
                owner: currentUser.name,
                ownerId: currentUser.id,
                participants: [
                  {
                    id: currentUser.id,
                    name: currentUser.name,
                    avatar: currentUser.avatar,
                    role: participant.role,
                    tasks: [{
                      id: task.id,
                      title: task.title,
                      progress: task.progress,
                      subtasks: task.subtasks
                    }]
                  }
                ],
                keyResults: taskKeyResults,
                totalProgress: taskTotalProgress,
                totalScore: taskTotalScore,
                createdDate: okr.createdDate
              });
            });
          }
        }
      });
      return currentUserOkrList;
    }
    
    const participantOkrList: OkrData[] = [];
    memberOkrList.forEach(okr => {
      if (okr.ownerId === selectedMember.value!.id) {
        participantOkrList.push(okr);
      } else {
        const participant = okr.participants.find(p => p.id === selectedMember.value!.id);
        if (participant && participant.tasks) {
          participant.tasks.forEach(task => {
            const taskKeyResults = task.subtasks.map(subtask => ({
              id: subtask.id,
              title: subtask.title,
              progress: subtask.progress,
              weight: Math.round(100 / task.subtasks.length),
              score: parseFloat((subtask.progress / 20).toFixed(1))
            }));
            
            const taskTotalProgress = task.subtasks.length > 0 
              ? Math.round(task.subtasks.reduce((sum, st) => sum + st.progress, 0) / task.subtasks.length)
              : task.progress;
            
            const taskTotalScore = taskKeyResults.length > 0
              ? parseFloat((taskKeyResults.reduce((sum, kr) => sum + kr.score, 0) / taskKeyResults.length).toFixed(1))
              : parseFloat((task.progress / 20).toFixed(1));
            
            participantOkrList.push({
                id: okr.id * 1000 + task.id,
                objective: task.title,
                owner: selectedMember.value!.name,
                ownerId: selectedMember.value!.id,
                participants: [
                  {
                    id: selectedMember.value!.id,
                    name: selectedMember.value!.name,
                    avatar: selectedMember.value!.avatar,
                    role: participant.role,
                    tasks: [{
                      id: task.id,
                      title: task.title,
                      progress: task.progress,
                      subtasks: task.subtasks
                    }]
                  }
                ],
                keyResults: taskKeyResults,
                totalProgress: taskTotalProgress,
                totalScore: taskTotalScore,
                createdDate: okr.createdDate
              });
          });
        }
      }
    });
    
    return participantOkrList;
  }
  return okrList.value;
});

const selectMember = (member: Member) => {
  selectedMember.value = member;
  viewingMyOkrs.value = false;
  scrollToTop();
};

const viewMyOkrs = () => {
  viewingMyOkrs.value = true;
  selectedMember.value = null;
  scrollToTop();
};

const viewAllOkrs = () => {
  selectedMember.value = null;
  viewingMyOkrs.value = false;
  scrollToTop();
};

const scrollToTop = () => {
  if (scrollContainer.value) {
    scrollContainer.value.scrollTop = 0;
  }
};

const handleSelectParticipant = (participant: IndexParticipant) => {
  const member: Member = {
    id: participant.id,
    name: participant.name,
    avatar: participant.avatar,
    department: '',
    role: participant.role
  };
  selectMember(member);
};

onMounted(() => {
  okrList.value = okrData;
});
</script>
