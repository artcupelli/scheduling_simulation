from batsim.batsim import BatsimScheduler
from procset import ProcSet
from itertools import islice

#
#   LONG PROCESSING TIME FIRST 
#   

class LPT(BatsimScheduler):

    def onAfterBatsimInit(self):
        self.jobs_waiting = []
        self.all_resources = self.bs.nb_compute_resources
        self.available_resources = ProcSet((0,self.all_resources-1))


    def scheduleJobs(self):
        jobs_to_execute = []

        ## Para cada JOB na fila
        for job in self.jobs_waiting:
            
            ## Verifica se há recursos disponíveis para rodá-lo
            if(job.requested_resources <= len(self.available_resources)):

                ## Reserva os recursos
                resources_allocated = ProcSet(*islice(self.available_resources, job.requested_resources))

                ## Aloca os recursos
                job.allocation = resources_allocated
                
                ## Adiciona na lista de JOBS para executar
                jobs_to_execute.append(job)

                ## Retira os recursos disponíveis
                self.available_resources -= resources_allocated

                ## Retira da fila de espera
                self.jobs_waiting.remove(job)

        ## Se tiver JOBs para executar, execute
        if (len(jobs_to_execute) > 0):
            self.bs.execute_jobs(jobs_to_execute)
        


    def onJobSubmission(self, job):

        ## Verifica se há recursos suficientes para o JOB
        if(job.requested_resources > self.all_resources):
            self.bs.reject_jobs([job])
            return

        ## Adiciona na lista de JOBs esperando
        self.addNewWaitingJob(job)

        ## Escalona
        self.scheduleJobs()


    def onJobCompletion(self, job):

        ## Retorna os recursos do JOB para disponível
        self.available_resources |= job.allocation
        
        ## Escalona novamente as tarefas
        self.scheduleJobs()


    def addNewWaitingJob(self, job):

        count = 0

        ## Verifica em qual posição da fila o novo JOB vai entrar
        while(count < len(self.jobs_waiting)):
            current_job = self.jobs_waiting[count]

            if(job.requested_time > current_job.requested_time):
                break

            count += 1


        ## Adiciona o novo JOB no índice correto
        if(len(self.jobs_waiting) == 0 or count == len(self.jobs_waiting)):
            self.jobs_waiting.append(job)  
        else:
            self.jobs_waiting.insert(count,job)

    
