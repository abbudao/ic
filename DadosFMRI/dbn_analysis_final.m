clear;
clc;

n_state=5;
alpha=0.9;
set_size=19;
nodes_to_use = [1 2 3 7 38];
%nodes_to_use = [4 5 6 8 39];
f=importdata('final_data.mat');
data=f.data;
names=f.names;

for i=1:size(data,3) %i.e. number of subjects
    ddata(:,:,i)=myIntervalDiscretize(data(:,nodes_to_use,i),n_state);
end
%%Replacement for myIntervalDiscretize? pandas.qcut?

for i=1:size(data,3)
    %[a,b]=multi_time_series_cat(ddata.T(:,:,[1:size(ddata,3)]~=i));
    ind=circshift(1:size(ddata,3),[0,-(i-1)]);
    %Pq faremos merge circularmente?
    tomerge = ddata(:,:,ismember(1:size(ddata,3),ind(1:set_size)));
    %Porque usar 1:19? 20 subjects?Não seria 0:19 ou 1:20?
    for j=1:size(tomerge,3)
        settomerge{j}=tomerge(:,:,j);
    end
    [a,b]=multi_time_series_cat(settomerge{:});
    
    tic;[best_net,bestscore]=globalMIT_ab(a,b,alpha,1);toc
    createDotGraphic(best_net,names(nodes_to_use),sprintf('fMRI DBN %d',i));
    saveas(gcf,sprintf('fMRI DBN %d',i),'png')
end
