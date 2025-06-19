import React, { useState } from 'react';
import {
  Container,
  Box,
  Typography,
  Stepper,
  Step,
  StepLabel,
  Paper,
  ThemeProvider,
  createTheme,
  CssBaseline,
} from '@mui/material';
import IncomeForm from './components/IncomeForm';
import SpendingForm from './components/SpendingForm';
import BenefitsForm from './components/BenefitsForm';
import Results from './components/Results';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
  components: {
    MuiStepIcon: {
      styleOverrides: {
        root: {
          '&.Mui-active': {
            color: '#1976d2',
          },
          '&.Mui-completed': {
            color: '#1976d2',
          },
        },
      },
    },
  },
});

const steps = ['Income', 'Spending Habits', 'Preferred Benefits'];

function App() {
  const [activeStep, setActiveStep] = useState(0);
  const [formData, setFormData] = useState({
    monthly_income: 0,
    spending_habits: {
      fuel: 0,
      travel: 0,
      groceries: 0,
      dining: 0,
    },
    preferred_benefits: [],
    existing_cards: [],
    credit_score: null,
  });

  const handleNext = () => {
    setActiveStep((prevStep) => prevStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevStep) => prevStep - 1);
  };

  const handleReset = () => {
    setActiveStep(0);
    setFormData({
      monthly_income: 0,
      spending_habits: {
        fuel: 0,
        travel: 0,
        groceries: 0,
        dining: 0,
      },
      preferred_benefits: [],
      existing_cards: [],
      credit_score: null,
    });
  };

  const getStepContent = (step: number) => {
    switch (step) {
      case 0:
        return (
          <IncomeForm
            formData={formData}
            setFormData={setFormData}
            onNext={handleNext}
          />
        );
      case 1:
        return (
          <SpendingForm
            formData={formData}
            setFormData={setFormData}
            onNext={handleNext}
            onBack={handleBack}
          />
        );
      case 2:
        return (
          <BenefitsForm
            formData={formData}
            setFormData={setFormData}
            onNext={handleNext}
            onBack={handleBack}
          />
        );
      default:
        return 'Unknown step';
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md">
        <Box sx={{ my: 4 }}>
          <Typography variant="h3" component="h1" gutterBottom align="center">
            Credit Card Recommender
          </Typography>
          <Paper sx={{ p: 3 }}>
            <Stepper 
              activeStep={activeStep} 
              sx={{ 
                mb: 4,
                '& .MuiStepLabel-iconContainer': {
                  '& .MuiStepIcon-root': {
                    color: 'primary.main',
                  },
                },
              }}
            >
              {steps.map((label) => (
                <Step key={label}>
                  <StepLabel>{label}</StepLabel>
                </Step>
              ))}
            </Stepper>
            {activeStep === steps.length ? (
              <Results formData={formData} onReset={handleReset} />
            ) : (
              getStepContent(activeStep)
            )}
          </Paper>
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;
